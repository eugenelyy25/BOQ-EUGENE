# BOQ-EUGENE
An Open-Source BOQ (Bill of Quantities) Data Analytics Template

## Overview

This repository provides a complete Power BI data engineering and visual analytics solution for transforming raw BOQ data into actionable insights. The solution includes data restructuring, exploratory data analysis (EDA), and an interactive dashboard for bid comparison.

## Features

✅ **Data Restructuring**
- Unpivots bidder columns from wide to long format
- Groups items by category (e.g., 01.xx → "General Works")
- Calculates total amounts per item and bidder

✅ **Exploratory Data Analysis (EDA)**
- Calculates total bid amounts per bidder
- Computes variance and standard deviation
- Identifies outliers and high-variance items
- Determines the lowest bidder automatically

✅ **Interactive Dashboard**
- Summary cards showing key metrics
- Matrix visualization for category-wise comparison
- Waterfall charts for bid breakdown
- User-adjustable quantity parameters for scenario analysis

## Repository Structure

```
BOQ-EUGENE/
├── README.md                       # This file
├── sample_boq_data.csv            # Sample raw BOQ data
├── data_transformation.py         # Python script for data processing
├── powerbi_setup_guide.md         # Comprehensive Power BI setup guide
├── dax_measures.txt               # DAX formulas for Power BI
├── boq_unpivoted.csv              # Transformed data (generated)
├── lowest_bidder_per_item.csv     # Lowest bidder analysis (generated)
├── item_variance_analysis.csv     # Variance analysis (generated)
└── boq_analysis_report.txt        # Summary report (generated)
```

## Quick Start

### Prerequisites

- Python 3.7+ with pandas and numpy
- Power BI Desktop (for dashboard creation)
- Microsoft Excel or CSV viewer

### Step 1: Run Data Transformation

```bash
# Install required Python packages
pip install pandas numpy

# Run the transformation script
python data_transformation.py
```

This will generate:
- `boq_unpivoted.csv` - Transformed data in long format
- `lowest_bidder_per_item.csv` - Item-level lowest bidder analysis
- `item_variance_analysis.csv` - Statistical variance analysis
- `boq_analysis_report.txt` - Summary report

### Step 2: Create Power BI Dashboard

1. Open Power BI Desktop
2. Follow the detailed instructions in `powerbi_setup_guide.md`
3. Import `boq_unpivoted.csv` or transform `sample_boq_data.csv` directly
4. Copy DAX measures from `dax_measures.txt`
5. Create visualizations as per the guide

## Data Structure

### Input Format (Wide Format)

| Item_Code | Description | Unit | Quantity | Bidder_A | Bidder_B | Bidder_C | Bidder_D |
|-----------|-------------|------|----------|----------|----------|----------|----------|
| 01.01 | Site Clearance | sqm | 1000 | 15.50 | 14.80 | 16.20 | 15.00 |
| 02.01 | Concrete Grade 30 | cum | 300 | 280.00 | 275.00 | 290.00 | 278.50 |

### Output Format (Long Format)

| Item_Code | Description | Unit | Quantity | Bidder | Unit_Rate | Category | Total_Amount |
|-----------|-------------|------|----------|--------|-----------|----------|--------------|
| 01.01 | Site Clearance | sqm | 1000 | Bidder_A | 15.50 | General Works | 15500.00 |
| 01.01 | Site Clearance | sqm | 1000 | Bidder_B | 14.80 | General Works | 14800.00 |

## Category Mapping

Items are automatically grouped into categories based on their item code prefix:

- **01.xx** → General Works
- **02.xx** → Concrete & Formwork
- **03.xx** → Masonry & Finishes
- **04.xx** → Tiling & Fixtures
- **05.xx** → Doors & Windows
- **06.xx** → Electrical Works
- **07.xx** → Plumbing & Drainage

## Key Metrics Calculated

1. **Total Bid Amount**: Sum of all items per bidder
2. **Lowest Bidder**: Bidder with the minimum total amount
3. **Variance Analysis**: Standard deviation and coefficient of variation
4. **Category Breakdown**: Cost breakdown by work category
5. **Outlier Detection**: Items with high price variance
6. **Competitive Analysis**: Comparison across all bidders

## Dashboard Components

### Page 1: Executive Summary
- Summary cards (Lowest Bidder, Lowest Bid Amount, etc.)
- Bidder comparison matrix
- Waterfall chart showing bid breakdown
- Bar chart for bidder comparison

### Page 2: Detailed Analysis
- Category breakdown chart
- Item-level detail table
- Variance analysis chart
- Outlier detection scatter plot

### Page 3: Scenario Planning
- Quantity adjustment slider
- Before/After comparison cards
- Adjusted bidder comparison chart
- Category impact analysis

## Customization

### Adding New Categories

Edit the `category_map` dictionary in `data_transformation.py`:

```python
category_map = {
    '01': 'General Works',
    '08': 'Your New Category',  # Add new mapping
    # ... existing mappings
}
```

### Adding More Bidders

Simply add new columns to `sample_boq_data.csv` following the naming pattern `Bidder_E`, `Bidder_F`, etc. The script will automatically detect and process them.

### Modifying DAX Measures

Edit `dax_measures.txt` to add custom calculations or KPIs specific to your needs.

## Sample Analysis Results

Based on the sample data:

- **Lowest Bidder**: Bidder_B ($444,830.00)
- **Highest Bidder**: Bidder_C ($483,920.00)
- **Bid Range**: $39,090.00 (8.8% variance)
- **Top Cost Category**: Concrete & Formwork (~37% of total)
- **High Variance Items**: Painting, Site Fencing, Excavation Works

## Best Practices

1. **Data Quality**: Ensure all numeric fields are populated
2. **Consistent Units**: Use standard units of measurement
3. **Regular Updates**: Refresh data as bids are received
4. **Documentation**: Keep track of assumptions and changes
5. **Backup**: Save versions of the Power BI file as you iterate

## Troubleshooting

### Issue: Categories showing as "Other"
**Solution**: Ensure Item_Code is formatted as string (e.g., "01.01" not 1.01)

### Issue: Python script fails
**Solution**: Check that pandas and numpy are installed: `pip install pandas numpy`

### Issue: Power BI not loading data
**Solution**: Verify CSV file encoding is UTF-8 and no special characters in paths

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

Template developed for YTL Database BOQ analysis requirements.

## Support

For questions or issues:
1. Check the `powerbi_setup_guide.md` for detailed instructions
2. Review the `dax_measures.txt` for formula references
3. Examine sample output files for expected results
