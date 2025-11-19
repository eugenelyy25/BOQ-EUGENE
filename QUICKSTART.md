# Quick Start Guide - BOQ Dashboard

Get your BOQ analysis dashboard up and running in 3 simple steps!

## ⚡ Fast Track (5 minutes)

### Step 1: Transform Your Data
```bash
# Install dependencies
pip install -r requirements.txt

# Run the transformation
python data_transformation.py
```

**Output:** You'll get 4 files ready for analysis:
- `boq_unpivoted.csv` - Transformed data
- `lowest_bidder_per_item.csv` - Item-level analysis  
- `item_variance_analysis.csv` - Statistical analysis
- `boq_analysis_report.txt` - Summary report

### Step 2: Open Power BI
1. Launch **Power BI Desktop**
2. Click **Get Data** → **Text/CSV**
3. Select `boq_unpivoted.csv`
4. Click **Load** (or **Transform Data** for customization)

### Step 3: Add Measures & Visualizations
1. Copy measures from `dax_measures.txt` into Power BI
2. Follow `powerbi_setup_guide.md` for dashboard layout
3. Create visuals as shown in `dashboard_mockup.md`

**Done!** You now have a working BOQ analysis dashboard.

---

## 📊 What You Get

### Instant Insights
✅ **Lowest Bidder**: Bidder_B at $444,830  
✅ **Bid Range**: $39,090 spread (8.8%)  
✅ **Cost Breakdown**: By category and bidder  
✅ **Outlier Detection**: High variance items identified  

### Interactive Dashboard
- 🎯 Summary cards with key metrics
- 📊 Matrix comparison across categories
- 💧 Waterfall chart showing cost buildup
- 📈 Detailed analysis with drill-down
- 🎚️ Quantity adjustment for scenarios

---

## 🎓 Learning Path

### Beginner
1. Read `README.md` for overview
2. Run `data_transformation.py` to see outputs
3. Import `boq_unpivoted.csv` into Power BI
4. Create basic visuals (cards, tables)

### Intermediate  
1. Study `powerbi_setup_guide.md` in detail
2. Implement all DAX measures from `dax_measures.txt`
3. Build the 3-page dashboard
4. Add interactivity and cross-filtering

### Advanced
1. Customize with `powerquery_m_script.txt`
2. Add your own categories and calculations
3. Integrate with live data sources
4. Create custom visuals and themes

---

## 📁 File Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| `sample_boq_data.csv` | Sample data | Testing, learning |
| `data_transformation.py` | Python transformation | Automated processing |
| `boq_unpivoted.csv` | Ready-to-use data | Quick Power BI import |
| `powerbi_setup_guide.md` | Complete tutorial | Building dashboard |
| `dax_measures.txt` | All formulas | Copy into Power BI |
| `powerquery_m_script.txt` | M language code | Advanced transformations |
| `dashboard_mockup.md` | Visual reference | Design guidance |
| `requirements.txt` | Python dependencies | Environment setup |

---

## 🔧 Common Tasks

### Change Category Names
Edit in `data_transformation.py`:
```python
category_map = {
    '01': 'Your New Name',  # Change this
    # ... more categories
}
```

### Add More Bidders
Just add columns to `sample_boq_data.csv`:
```
Item_Code,Description,...,Bidder_E,Bidder_F
```
Script automatically detects all `Bidder_*` columns!

### Adjust Dashboard Colors
In Power BI:
- Format → Colors → Choose theme
- Or customize each visual individually

### Export Results
From Power BI:
- File → Export → PDF (full report)
- Visual → More options → Export data (tables)

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install pandas numpy
```

### Categories show as "Other"
Check that Item_Code is formatted as "01.01" (with leading zero)

### Power BI won't load CSV
- Ensure file encoding is UTF-8
- Check file path has no special characters
- Try "Get Data" → "Text/CSV" instead of drag-drop

### Measures not working
- Verify table name matches (change `BOQ_Data` to your table name)
- Check data types (numbers must be numeric, not text)
- Refresh data model

---

## 💡 Tips & Tricks

1. **Start Simple**: Load data first, add complexity later
2. **Save Often**: Save Power BI file after each major change
3. **Test with Sample**: Use provided sample data before your real data
4. **Document Changes**: Keep notes on customizations
5. **Backup**: Save versions with dates (BOQ_v1, BOQ_v2...)

---

## 🎯 Next Steps

After completing the quick start:

1. **Customize**: Adapt to your specific BOQ structure
2. **Extend**: Add more categories, bidders, or metrics
3. **Share**: Publish to Power BI Service for team access
4. **Automate**: Set up data refresh schedules
5. **Learn**: Explore advanced Power BI features

---

## 📚 Additional Resources

- Full documentation: `README.md`
- Detailed guide: `powerbi_setup_guide.md`
- Visual reference: `dashboard_mockup.md`
- Python code: `data_transformation.py`
- Power Query: `powerquery_m_script.txt`
- DAX formulas: `dax_measures.txt`

---

## 🆘 Need Help?

1. Check the troubleshooting section above
2. Review the detailed setup guide
3. Verify your data matches the expected format
4. Test with the provided sample data first
5. Create an issue in the GitHub repository

---

## ✅ Checklist

Before you start:
- [ ] Python 3.7+ installed
- [ ] Power BI Desktop installed
- [ ] Sample data reviewed
- [ ] Requirements installed (`pip install -r requirements.txt`)

After quick start:
- [ ] Data transformation ran successfully
- [ ] CSV loaded into Power BI
- [ ] Basic visuals created
- [ ] Dashboard functional

Ready to advance:
- [ ] All DAX measures added
- [ ] 3-page dashboard complete
- [ ] Interactivity configured
- [ ] Custom data imported

---

**Time Investment:**
- Quick Start: 5-10 minutes
- Basic Dashboard: 30-45 minutes  
- Complete Solution: 2-3 hours
- Mastery: Ongoing

**Start now and have your BOQ insights in minutes!** 🚀
