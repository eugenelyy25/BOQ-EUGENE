"""
BOQ Data Transformation Script
This script performs data restructuring including unpivoting bidders and grouping items
"""

import pandas as pd
import numpy as np

def load_boq_data(filepath):
    """Load BOQ data from CSV file"""
    return pd.read_csv(filepath, dtype={'Item_Code': str})

def extract_category(item_code):
    """Extract category from item code (e.g., 01.xx -> General)"""
    category_map = {
        '01': 'General Works',
        '02': 'Concrete & Formwork',
        '03': 'Masonry & Finishes',
        '04': 'Tiling & Fixtures',
        '05': 'Doors & Windows',
        '06': 'Electrical Works',
        '07': 'Plumbing & Drainage'
    }
    
    # Convert to string and extract prefix
    item_code_str = str(item_code)
    prefix = item_code_str.split('.')[0]
    return category_map.get(prefix, 'Other')

def unpivot_bidders(df):
    """
    Unpivot bidder columns to create a long-format dataframe
    Transforms wide format (Bidder_A, Bidder_B, ...) to long format
    """
    # Get bidder columns
    bidder_cols = [col for col in df.columns if col.startswith('Bidder_')]
    
    # Create unpivoted dataframe
    id_vars = ['Item_Code', 'Description', 'Unit', 'Quantity']
    df_unpivoted = df.melt(
        id_vars=id_vars,
        value_vars=bidder_cols,
        var_name='Bidder',
        value_name='Unit_Rate'
    )
    
    # Add category column
    df_unpivoted['Category'] = df_unpivoted['Item_Code'].apply(extract_category)
    
    # Calculate total amount
    df_unpivoted['Total_Amount'] = df_unpivoted['Quantity'] * df_unpivoted['Unit_Rate']
    
    return df_unpivoted

def calculate_statistics(df_unpivoted):
    """
    Calculate key statistics for EDA:
    - Total bid amount per bidder
    - Variance analysis
    - Lowest bidder identification
    """
    stats = {}
    
    # Total bid amount per bidder
    bidder_totals = df_unpivoted.groupby('Bidder')['Total_Amount'].sum().sort_values()
    stats['bidder_totals'] = bidder_totals
    stats['lowest_bidder'] = bidder_totals.idxmin()
    stats['lowest_amount'] = bidder_totals.min()
    
    # Category-wise totals per bidder
    category_totals = df_unpivoted.pivot_table(
        values='Total_Amount',
        index='Category',
        columns='Bidder',
        aggfunc='sum'
    )
    stats['category_totals'] = category_totals
    
    # Variance analysis per item
    item_variance = df_unpivoted.groupby('Item_Code').agg({
        'Unit_Rate': ['mean', 'std', 'min', 'max'],
        'Total_Amount': ['mean', 'std']
    })
    item_variance.columns = ['_'.join(col).strip() for col in item_variance.columns.values]
    stats['item_variance'] = item_variance
    
    # Identify outliers (items with high variance)
    item_variance['cv'] = item_variance['Unit_Rate_std'] / item_variance['Unit_Rate_mean']
    stats['high_variance_items'] = item_variance.nlargest(5, 'cv')
    
    return stats

def identify_lowest_bidder_per_item(df_unpivoted):
    """Identify the lowest bidder for each item"""
    lowest_per_item = df_unpivoted.loc[
        df_unpivoted.groupby('Item_Code')['Unit_Rate'].idxmin()
    ][['Item_Code', 'Description', 'Bidder', 'Unit_Rate', 'Total_Amount']]
    
    return lowest_per_item

def generate_summary_report(df, df_unpivoted, stats):
    """Generate a comprehensive summary report"""
    report = []
    report.append("=" * 80)
    report.append("BOQ ANALYSIS SUMMARY REPORT")
    report.append("=" * 80)
    report.append("")
    
    report.append("BIDDER COMPARISON:")
    report.append("-" * 40)
    for bidder, total in stats['bidder_totals'].items():
        report.append(f"{bidder}: ${total:,.2f}")
    report.append("")
    report.append(f"LOWEST BIDDER: {stats['lowest_bidder']} (${stats['lowest_amount']:,.2f})")
    report.append("")
    
    report.append("CATEGORY-WISE BREAKDOWN:")
    report.append("-" * 40)
    report.append(stats['category_totals'].to_string())
    report.append("")
    
    report.append("HIGH VARIANCE ITEMS (Top 5):")
    report.append("-" * 40)
    report.append(stats['high_variance_items'][['Unit_Rate_mean', 'Unit_Rate_std', 'cv']].to_string())
    report.append("")
    
    return "\n".join(report)

def main():
    """Main execution function"""
    # Load data
    print("Loading BOQ data...")
    df = load_boq_data('sample_boq_data.csv')
    print(f"Loaded {len(df)} items")
    
    # Unpivot bidders
    print("\nUnpivoting bidder data...")
    df_unpivoted = unpivot_bidders(df)
    print(f"Unpivoted data shape: {df_unpivoted.shape}")
    
    # Save unpivoted data
    df_unpivoted.to_csv('boq_unpivoted.csv', index=False)
    print("Saved unpivoted data to boq_unpivoted.csv")
    
    # Calculate statistics
    print("\nCalculating statistics...")
    stats = calculate_statistics(df_unpivoted)
    
    # Identify lowest bidder per item
    lowest_per_item = identify_lowest_bidder_per_item(df_unpivoted)
    lowest_per_item.to_csv('lowest_bidder_per_item.csv', index=False)
    print("Saved lowest bidder analysis to lowest_bidder_per_item.csv")
    
    # Generate and save summary report
    report = generate_summary_report(df, df_unpivoted, stats)
    print("\n" + report)
    
    with open('boq_analysis_report.txt', 'w') as f:
        f.write(report)
    print("\nSaved analysis report to boq_analysis_report.txt")
    
    # Save detailed statistics
    stats['item_variance'].to_csv('item_variance_analysis.csv')
    print("Saved variance analysis to item_variance_analysis.csv")
    
    print("\nData transformation completed successfully!")

if __name__ == "__main__":
    main()
