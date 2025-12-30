# charts_master_df_ALP2.py
# Generates charts comparing trades and items costs from master_df_export_ALP2_2025-11-19.csv

import re
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', context='talk')

REPO_ROOT = Path(__file__).resolve().parent
CSV_PATH = REPO_ROOT / 'master_df_export_ALP2_2025-11-19.csv'
OUT_DIR = REPO_ROOT / 'reports'
OUT_DIR.mkdir(exist_ok=True)

# Helper to find header row (the CSV contains a short export summary at top)
def load_master_df(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header_idx = None
    for i, line in enumerate(lines[:50]):
        if re.match(r"\s*Project\s*,\s*Type\s*,\s*Trade", line, flags=re.I):
            header_idx = i
            break
    if header_idx is None:
        # fallback: try to read normally
        df = pd.read_csv(csv_path)
        return df

    # Read CSV from header row
    df = pd.read_csv(csv_path, skiprows=header_idx)
    return df


df = load_master_df(CSV_PATH)
print(f'Loaded dataframe with {len(df)} rows and columns: {list(df.columns)}')

# Clean numeric columns
for col in ['Rate','Total_Amount','Qty']:
    if col in df.columns:
        df[col] = (df[col].astype(str)
                   .str.replace(',', '')
                   .str.replace('\$', '')
                   .str.strip())
        df.loc[df[col].str.lower().isin(['nan','none','', ' - ', '-']), col] = None
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Ensure Trade column exists
if 'Trade' not in df.columns:
    raise SystemExit('Trade column not found in CSV')

# 1) Total cost per Trade (sum of Total_Amount)
trade_totals = df.groupby('Trade', dropna=False)['Total_Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
ax = trade_totals.plot(kind='bar', color='tab:blue')
ax.set_ylabel('Total Amount (RM)')
ax.set_title('Total Cost per Trade (ALP2)')
plt.tight_layout()
plt.savefig(OUT_DIR / 'total_cost_per_trade.png', dpi=150)
plt.close()

# 2) Top 20 cost items across all trades
if 'Standardized_Item' in df.columns:
    item_totals = (df.groupby('Standardized_Item')['Total_Amount']
                   .sum()
                   .dropna()
                   .sort_values(ascending=False).head(20))
    plt.figure(figsize=(12,8))
    sns.barplot(y=item_totals.index, x=item_totals.values, palette='viridis')
    plt.xlabel('Total Amount (RM)')
    plt.title('Top 20 Items by Total Cost (ALP2)')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'top20_items_by_cost.png', dpi=150)
    plt.close()
else:
    print('Standardized_Item column not found — skipping top items chart')

# 3) Rate distribution per Trade (boxplot)
if 'Rate' in df.columns:
    rate_df = df[['Trade','Rate']].dropna()
    plt.figure(figsize=(12,8))
    # Keep only trades with some data
    trades_with_rate = rate_df['Trade'].value_counts().loc[lambda x: x>0].index
    sns.boxplot(data=rate_df, x='Trade', y='Rate')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Rate (RM)')
    plt.title('Rate Distribution per Trade')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'rate_distribution_per_trade.png', dpi=150)
    plt.close()
else:
    print('Rate column not found — skipping rate distribution chart')

# 4) Heatmap: subcontractor vs trade totals
if 'Subcon_Name' in df.columns:
    pivot = (df.pivot_table(index='Subcon_Name', columns='Trade', values='Total_Amount', aggfunc='sum')
             .fillna(0))
    # Normalize for better color scaling
    plt.figure(figsize=(14, max(6, pivot.shape[0]*0.25)))
    sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlGnBu')
    plt.title('Subcontractor vs Trade Total Amounts (RM)')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'subcon_vs_trade_heatmap.png', dpi=150)
    plt.close()
else:
    print('Subcon_Name column not found — skipping heatmap')

print('Charts generated and saved in:', OUT_DIR)
