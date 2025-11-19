# Power BI Dashboard Mockup and Layout Guide

## Dashboard Overview

The BOQ Dashboard consists of 3 main pages, each serving a specific purpose in the bid analysis workflow.

---

## Page 1: Executive Summary

### Layout Structure
```
┌─────────────────────────────────────────────────────────────────────┐
│  BOQ DASHBOARD - Executive Summary                          [Filters]│
├─────────────┬──────────────┬──────────────┬──────────────┬──────────┤
│   LOWEST    │   LOWEST     │   AVERAGE    │    TOTAL     │   BID    │
│   BIDDER    │   BID AMT    │   BID AMT    │    ITEMS     │  RANGE   │
│             │              │              │              │          │
│  Bidder_B   │  $444,830    │  $461,444    │     21       │ $39,090  │
│   [GREEN]   │              │              │              │          │
└─────────────┴──────────────┴──────────────┴──────────────┴──────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  BIDDER COMPARISON MATRIX                                            │
├───────────────────────┬──────────┬──────────┬──────────┬──────────┤
│ Category              │ Bidder_A │ Bidder_B │ Bidder_C │ Bidder_D │
├───────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ General Works         │ $45,000  │ $42,650* │ $47,700  │ $43,900  │
│ Concrete & Formwork   │$171,500  │$165,800* │$178,300  │$168,750  │
│ Masonry & Finishes    │ $69,000  │ $66,000* │ $73,200  │ $67,920  │
│ Tiling & Fixtures     │ $58,250  │ $56,200* │ $60,725  │ $57,375  │
│ Doors & Windows       │ $51,100  │ $49,250* │ $52,950  │ $50,390  │
│ Electrical Works      │ $28,700  │ $27,730* │ $29,920  │ $28,265  │
│ Plumbing & Drainage   │ $38,800  │ $37,200* │ $41,125  │ $38,075  │
├───────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ TOTAL                 │$462,350  │$444,830  │$483,920  │$454,675  │
└───────────────────────┴──────────┴──────────┴──────────┴──────────┘
* = Lowest in row (Green shading)

┌─────────────────────────────────┬───────────────────────────────────┐
│  WATERFALL CHART               │  BAR CHART - Total by Bidder      │
│  Cumulative Bid Breakdown      │                                   │
│                                 │  Bidder_B ████████████ $444,830  │
│  Start                          │  Bidder_D ████████████▌ $454,675 │
│    ║                           │  Bidder_A █████████████ $462,350  │
│    ║ +Gen Works                 │  Bidder_C █████████████▌ $483,920│
│    ║ +Concrete                  │                                   │
│    ║ +Masonry                   │  [Sorted ascending by amount]     │
│    ║ +Tiling                    │                                   │
│    ║ +Doors                     │                                   │
│    ║ +Electrical                │                                   │
│    ║ +Plumbing                  │                                   │
│    ▼                           │                                   │
│  Total                          │                                   │
└─────────────────────────────────┴───────────────────────────────────┘
```

### Color Scheme
- **Lowest Bidder**: Green highlight
- **Mid-range**: Yellow/Orange
- **Highest**: Red
- **Matrix cells**: Gradient from green (low) to red (high)

---

## Page 2: Detailed Analysis

### Layout Structure
```
┌─────────────────────────────────────────────────────────────────────┐
│  DETAILED ANALYSIS                                        [Filters]  │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  CATEGORY BREAKDOWN - Stacked Column Chart                          │
│                                                                      │
│  Amount                                                              │
│  $180K ├──┐                                                         │
│  $160K │  █ Bidder_D                                                │
│  $140K │  █ Bidder_C                                                │
│  $120K │  █ Bidder_B                                                │
│  $100K │  █ Bidder_A                                                │
│   $80K │  █                                                          │
│   $60K │  █  █                                                       │
│   $40K │  █  █  █  █  █  █  █                                       │
│   $20K │  █  █  █  █  █  █  █                                       │
│      0 └──┴──┴──┴──┴──┴──┴──                                       │
│         Gen Con Mas Til Dor Ele Plu                                 │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  ITEM-LEVEL DETAIL TABLE                                            │
├──────┬────────────────────┬─────────┬────┬──────────┬──────────┬───┤
│ Code │ Description        │Category │Qty │ Bidder_A │ Bidder_B │...│
├──────┼────────────────────┼─────────┼────┼──────────┼──────────┼───┤
│01.01 │Site Clearance      │General  │1000│   15.50  │  14.80*  │...│
│01.02 │Excavation Works    │General  │ 500│   45.00  │  42.50*  │...│
│02.01 │Concrete Grade 30   │Concrete │ 300│  280.00  │ 275.00*  │...│
│...   │...                 │...      │... │  ...     │  ...     │...│
└──────┴────────────────────┴─────────┴────┴──────────┴──────────┴───┘
* = Lowest rate (highlighted)

┌─────────────────────────────────┬───────────────────────────────────┐
│  VARIANCE ANALYSIS             │  OUTLIER DETECTION                │
│  Line & Column Chart            │  Scatter Plot                     │
│                                 │                                   │
│  Rate  ┌─o─────o────o──────o  │  Total  ╱                        │
│   $300 │ │▌    │▌   │▌    │▌  │   Amt   │    ●                     │
│   $250 │ │▌    │▌   │▌    │▌  │ $100K   │  ●   ●                   │
│   $200 │ │▌    │▌   │▌    │▌  │         │●   ●   ●                 │
│   $150 │ │▌    │▌   │▌    │▌  │  $50K   │  ●●  ●●●                 │
│   $100 │ │▌    │▌   │▌    │▌  │         │ ●● ●●●●●                 │
│    $50 │ │▌    │▌   │▌    │▌  │    $0   └──────────────           │
│     $0 └─┴─────┴────┴──────┴   │           $0  Rate  $400          │
│        01.01 02.01 03.01 04.01 │   Size = Quantity                 │
│        ▌A ▌B ▌C ▌D  -o- Avg    │   Color = Bidder                  │
└─────────────────────────────────┴───────────────────────────────────┘
```

---

## Page 3: Scenario Planning with Quantity Adjustment

### Layout Structure
```
┌─────────────────────────────────────────────────────────────────────┐
│  SCENARIO PLANNING - Quantity Adjustment Analysis                   │
├─────────────────────────────────────────────────────────────────────┤
│  Adjust Quantity:  [50%] ◄─────●─────► [200%]  Current: 100%       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────┬─────────────┬──────────────┬──────────────────────────┐
│  ORIGINAL   │  ADJUSTED   │  DIFFERENCE  │  % CHANGE                │
│  TOTAL      │  TOTAL      │              │                          │
│             │             │              │                          │
│ $444,830    │ $444,830    │     $0       │      0%                  │
│  [Blue]     │  [Orange]   │              │                          │
└─────────────┴─────────────┴──────────────┴──────────────────────────┘
(Values update dynamically based on slider position)

┌─────────────────────────────────────────────────────────────────────┐
│  BIDDER COMPARISON - Original vs Adjusted                           │
│                                                                      │
│  Bidder_A   ████████████ $462,350                                   │
│             ████████████ $462,350 (100%)                            │
│                                                                      │
│  Bidder_B   ███████████ $444,830                                    │
│             ███████████ $444,830 (100%)                             │
│                                                                      │
│  Bidder_C   █████████████ $483,920                                  │
│             █████████████ $483,920 (100%)                           │
│                                                                      │
│  Bidder_D   ████████████ $454,675                                   │
│             ████████████ $454,675 (100%)                            │
│                                                                      │
│  ▌ Original  ▌ Adjusted                                             │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  CATEGORY IMPACT ANALYSIS - Matrix                                  │
├────────────────────────┬───────────┬───────────┬───────────┬────────┤
│ Category               │ Bidder_A  │ Bidder_B  │ Bidder_C  │Bidder_D│
├────────────────────────┼───────────┼───────────┼───────────┼────────┤
│ General Works          │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Concrete & Formwork    │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Masonry & Finishes     │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Tiling & Fixtures      │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Doors & Windows        │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Electrical Works       │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
│ Plumbing & Drainage    │   $0 (0%) │   $0 (0%) │   $0 (0%) │  $0 (0%)│
└────────────────────────┴───────────┴───────────┴───────────┴────────┘
Shows impact of quantity changes on each category/bidder combination
```

### Interactive Elements

#### Quantity Adjustment Slider
- **Min**: 50% (half quantities)
- **Max**: 200% (double quantities)
- **Default**: 100% (original)
- **Step**: 10%

When slider moves:
- All "Adjusted" values update in real-time
- Difference calculations update automatically
- Charts refresh to show new comparisons
- Color coding adjusts based on new values

---

## Interactivity Features

### Cross-Filtering
- Click any category → filters all visuals to that category
- Click any bidder → highlights that bidder across all charts
- Click any item → shows details in all related visuals

### Drill-Through
- Right-click any data point → "Drill through" → Item Details
- Shows comprehensive information about selected item/category

### Tooltips
Hover over any visual element to see:
- Detailed breakdowns
- Comparison to average/lowest
- Percentage of total
- Ranking information

### Filters Panel (Always Visible)
```
┌──────────────────────┐
│ FILTERS              │
├──────────────────────┤
│ □ Bidder            │
│   ☑ Bidder_A        │
│   ☑ Bidder_B        │
│   ☑ Bidder_C        │
│   ☑ Bidder_D        │
│                      │
│ □ Category          │
│   ☑ All Categories   │
│                      │
│ □ Item Code         │
│   [Search...]        │
│                      │
│ □ Amount Range      │
│   ◄──────●──────►   │
└──────────────────────┘
```

---

## Design Principles

### Color Palette
- **Primary**: Blue (#0078D4) - Headers, primary bars
- **Success**: Green (#107C10) - Lowest/best values
- **Warning**: Orange (#FF8C00) - Mid-range values
- **Danger**: Red (#E81123) - Highest values
- **Neutral**: Gray (#8A8886) - Labels, text

### Typography
- **Headers**: Segoe UI Bold, 18-24pt
- **Cards**: Segoe UI Semibold, 32-48pt
- **Labels**: Segoe UI Regular, 10-12pt
- **Data**: Segoe UI Regular, 11pt

### Spacing
- Card padding: 10-15px
- Section spacing: 20px
- Visual margins: 10px
- Page margins: 20px all sides

### Accessibility
- All charts include data labels
- Color-blind friendly palette option
- High contrast mode available
- Screen reader compatible
- Keyboard navigation enabled

---

## Export Options

Users can export:
1. **Full Report**: PDF with all 3 pages
2. **Summary View**: Page 1 as PNG/PDF
3. **Detailed Data**: Excel export of underlying data
4. **Analysis Results**: CSV of calculated metrics

---

## Performance Optimization

- Use DirectQuery for large datasets
- Implement aggregations for common queries
- Cache frequently accessed calculations
- Minimize use of calculated columns
- Optimize DAX formulas for speed

---

## Mobile Layout

Responsive design automatically adjusts for mobile:
- Cards stack vertically
- Charts resize appropriately
- Filters move to collapsible menu
- Touch-friendly controls
- Simplified views for small screens
