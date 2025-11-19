# Power BI BOQ Dashboard Setup Guide

## Overview
This guide provides step-by-step instructions for setting up the BOQ (Bill of Quantities) comparison dashboard in Power BI.

## Data Structure

### Input Data
The raw BOQ data is in wide format with columns:
- `Item_Code`: Unique identifier for each work item
- `Description`: Description of the work item
- `Unit`: Unit of measurement
- `Quantity`: Quantity required
- `Bidder_A`, `Bidder_B`, `Bidder_C`, `Bidder_D`: Unit rates from each bidder

### Transformed Data
After transformation, data is in long format with:
- `Item_Code`, `Description`, `Unit`, `Quantity`
- `Bidder`: Name of the bidder
- `Unit_Rate`: Rate per unit
- `Category`: Grouped category (e.g., "General Works", "Concrete & Formwork")
- `Total_Amount`: Calculated as Quantity × Unit_Rate

## Power BI Setup Steps

### 1. Import Data

#### Option A: Import CSV Files Directly
1. Open Power BI Desktop
2. Click "Get Data" → "Text/CSV"
3. Select `sample_boq_data.csv`
4. Click "Transform Data" to open Power Query Editor

#### Option B: Use Pre-transformed Data
1. Run the Python transformation script first:
   ```bash
   python data_transformation.py
   ```
2. Import `boq_unpivoted.csv` into Power BI

### 2. Data Transformation in Power Query

If importing raw data directly, perform these transformations:

#### A. Unpivot Bidder Columns
1. Select `Item_Code`, `Description`, `Unit`, `Quantity` columns
2. Right-click and select "Unpivot Other Columns"
3. Rename new columns:
   - `Attribute` → `Bidder`
   - `Value` → `Unit_Rate`

#### B. Add Category Column
1. Add Custom Column with formula:
   ```
   if Text.Start([Item_Code], 2) = "01" then "General Works"
   else if Text.Start([Item_Code], 2) = "02" then "Concrete & Formwork"
   else if Text.Start([Item_Code], 2) = "03" then "Masonry & Finishes"
   else if Text.Start([Item_Code], 2) = "04" then "Tiling & Fixtures"
   else if Text.Start([Item_Code], 2) = "05" then "Doors & Windows"
   else if Text.Start([Item_Code], 2) = "06" then "Electrical Works"
   else if Text.Start([Item_Code], 2) = "07" then "Plumbing & Drainage"
   else "Other"
   ```
2. Name the column `Category`

#### C. Add Calculated Total Amount
1. Add Custom Column: `Total_Amount = [Quantity] * [Unit_Rate]`
2. Ensure data types are correct:
   - `Quantity`: Whole Number
   - `Unit_Rate`: Decimal Number
   - `Total_Amount`: Decimal Number

#### D. Close & Apply
Click "Close & Apply" to load data into Power BI

### 3. Create Measures

Create the following DAX measures for analysis:

```dax
// Total Bid Amount
Total Bid Amount = SUM(BOQ_Data[Total_Amount])

// Average Unit Rate
Average Unit Rate = AVERAGE(BOQ_Data[Unit_Rate])

// Lowest Bid Amount
Lowest Bid = 
MINX(
    SUMMARIZE(BOQ_Data, BOQ_Data[Bidder], "Total", SUM(BOQ_Data[Total_Amount])),
    [Total]
)

// Lowest Bidder Name
Lowest Bidder = 
VAR MinTotal = [Lowest Bid]
RETURN
CALCULATE(
    SELECTEDVALUE(BOQ_Data[Bidder]),
    FILTER(
        ALL(BOQ_Data[Bidder]),
        CALCULATE(SUM(BOQ_Data[Total_Amount])) = MinTotal
    )
)

// Variance from Lowest
Variance from Lowest = 
VAR CurrentTotal = [Total Bid Amount]
VAR LowestTotal = [Lowest Bid]
RETURN
CurrentTotal - LowestTotal

// Percentage Variance
Percentage Variance = 
DIVIDE([Variance from Lowest], [Lowest Bid], 0) * 100

// Item Count
Item Count = DISTINCTCOUNT(BOQ_Data[Item_Code])

// Average Item Amount
Average Item Amount = DIVIDE([Total Bid Amount], [Item Count], 0)
```

### 4. Create Parameters for User Adjustments

#### A. Quantity Adjustment Parameter
1. Go to "Modeling" → "New Parameter"
2. Set up parameter:
   - Name: `Quantity Adjustment %`
   - Data Type: Decimal Number
   - Minimum: 0.5 (50%)
   - Maximum: 2.0 (200%)
   - Increment: 0.1 (10%)
   - Default: 1.0 (100%)
3. Add a slicer to the dashboard for this parameter

#### B. Create Adjusted Measures
```dax
// Adjusted Quantity
Adjusted Quantity = 
BOQ_Data[Quantity] * 'Quantity Adjustment %'[Quantity Adjustment % Value]

// Adjusted Total Amount
Adjusted Total Amount = 
SUMX(
    BOQ_Data,
    BOQ_Data[Unit_Rate] * [Adjusted Quantity]
)
```

### 5. Dashboard Design

Create a multi-page dashboard with the following visualizations:

#### Page 1: Executive Summary

##### A. Summary Cards (Top Row)
Create 5 card visuals:
1. **Lowest Bidder Card**
   - Measure: `Lowest Bidder`
   - Format: Text, large font, highlight color

2. **Lowest Bid Amount Card**
   - Measure: `Lowest Bid`
   - Format: Currency, $#,##0

3. **Average Bid Card**
   - Measure: `Average([Total Bid Amount])`
   - Format: Currency

4. **Total Items Card**
   - Measure: `Item Count`
   - Format: Whole number

5. **Bid Range Card**
   - Measure: `MAX([Total Bid Amount]) - MIN([Total Bid Amount])`
   - Format: Currency

##### B. Bidder Comparison Matrix
1. Add Matrix visual
2. Rows: `Category`
3. Columns: `Bidder`
4. Values: `Total_Amount` (sum)
5. Formatting:
   - Enable background color gradient (lowest = green, highest = red)
   - Show row totals and column totals
   - Format as currency

##### C. Waterfall Chart - Bid Breakdown
1. Add Waterfall chart visual
2. Category: `Bidder`
3. Y Axis: `Total Bid Amount`
4. Breakdown: Shows cumulative bid differences
5. Format: Show connecting lines, data labels

##### D. Bar Chart - Bidder Comparison
1. Add Clustered Bar Chart
2. Y-axis: `Bidder`
3. X-axis: `Total Bid Amount`
4. Data labels: Show values
5. Sort: Ascending by amount

#### Page 2: Detailed Analysis

##### A. Category Breakdown
1. Add Stacked Column Chart
2. X-axis: `Category`
3. Y-axis: `Total_Amount`
4. Legend: `Bidder`
5. Title: "Bid Amount by Category"

##### B. Item-Level Detail Table
1. Add Table visual
2. Columns:
   - `Item_Code`
   - `Description`
   - `Category`
   - `Quantity`
   - Create columns for each bidder's unit rate
   - Create column for lowest rate (highlight)
3. Enable filters and sorting

##### C. Variance Analysis Chart
1. Add Line and Clustered Column Chart
2. X-axis: `Item_Code`
3. Column values: `Unit_Rate` by `Bidder`
4. Line values: `AVERAGE(Unit_Rate)`
5. Title: "Unit Rate Variance by Item"

##### D. Outlier Detection
1. Add Scatter Chart
2. X-axis: `Unit_Rate`
3. Y-axis: `Total_Amount`
4. Legend: `Bidder`
5. Size: `Quantity`
6. Enable highlighting of items with high variance

#### Page 3: Quantity Adjustment Scenario

##### A. Quantity Adjustment Slicer
1. Add Slicer for `Quantity Adjustment %`
2. Style: Slider
3. Position: Top of page

##### B. Comparison Cards (Before/After)
Create cards showing:
1. Original Total (using `Total Bid Amount`)
2. Adjusted Total (using `Adjusted Total Amount`)
3. Difference
4. Percentage Change

##### C. Adjusted Bidder Comparison
1. Add Clustered Bar Chart
2. Y-axis: `Bidder`
3. X-axis: 
   - `Total Bid Amount` (Original)
   - `Adjusted Total Amount` (Adjusted)
4. Legend: Show both values side by side

##### D. Category Impact Analysis
1. Add Matrix or Table
2. Rows: `Category`
3. Columns: `Bidder`
4. Values: `Adjusted Total Amount` - `Total Bid Amount`
5. Format: Show differences with conditional formatting

### 6. Formatting and Interactivity

#### Visual Interactions
1. Enable cross-filtering between all visuals
2. Set up drill-through from summary to detail pages
3. Add bookmarks for different views:
   - Overview
   - Lowest Bidder Focus
   - High Variance Items

#### Conditional Formatting
1. Matrix: Apply color scales
   - Lowest value: Green (good)
   - Highest value: Red (expensive)

2. Table: Apply data bars for amount columns

3. Cards: Use appropriate background colors
   - Lowest bidder: Green
   - Others: Blue/Gray

#### Tooltips
Create custom tooltips showing:
- Item details
- Bid comparison
- Category totals

### 7. Publish and Share

1. Save the Power BI file as `BOQ_Dashboard.pbix`
2. Publish to Power BI Service (if required)
3. Set up scheduled refresh if using live data
4. Share with stakeholders with appropriate permissions

## Key Features

### Interactive Elements
- ✅ Click on any category to filter all visuals
- ✅ Use slicers to filter by date, category, or bidder
- ✅ Adjust quantities dynamically to see impact on totals
- ✅ Drill through from summary to detail views

### Analysis Capabilities
- ✅ Identify lowest bidder instantly
- ✅ Compare bids across categories
- ✅ Analyze variance and outliers
- ✅ Scenario planning with quantity adjustments
- ✅ Export data for further analysis

## Troubleshooting

### Issue: Unpivot not working
**Solution**: Ensure all bidder columns have the same data type (Decimal)

### Issue: Totals not matching
**Solution**: Check for blank values and handle with COALESCE or ISBLANK

### Issue: Parameter not updating visuals
**Solution**: Ensure measures reference the parameter value correctly

### Issue: Formatting not applied
**Solution**: Refresh data and reapply formatting; check data types

## Best Practices

1. **Data Quality**: Ensure clean data with no null values in critical columns
2. **Performance**: Use measures instead of calculated columns where possible
3. **Naming**: Use clear, descriptive names for measures and columns
4. **Documentation**: Add descriptions to measures for team understanding
5. **Version Control**: Save different versions as you iterate
6. **Testing**: Test with different data scenarios before production use

## Next Steps

1. Customize the dashboard colors to match company branding
2. Add additional KPIs as needed
3. Set up data refresh schedule
4. Create user documentation
5. Train stakeholders on dashboard usage
6. Gather feedback and iterate

## Support

For issues or enhancements:
- Review Power BI documentation: https://docs.microsoft.com/power-bi/
- Check DAX function reference: https://dax.guide/
- Community support: https://community.powerbi.com/
