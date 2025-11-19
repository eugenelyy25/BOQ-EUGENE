"""
Validation Script for BOQ Project Setup
Checks that all files are present and data is correct
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and print status"""
    exists = os.path.isfile(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filepath}")
    return exists

def validate_csv_structure(filepath, expected_columns):
    """Validate CSV has expected columns"""
    try:
        with open(filepath, 'r') as f:
            header = f.readline().strip()
            columns = header.split(',')
            
        missing = set(expected_columns) - set(columns)
        if missing:
            print(f"  ✗ Missing columns: {missing}")
            return False
        else:
            print(f"  ✓ All expected columns present")
            return True
    except Exception as e:
        print(f"  ✗ Error reading file: {e}")
        return False

def main():
    """Run all validation checks"""
    print("=" * 70)
    print("BOQ PROJECT VALIDATION")
    print("=" * 70)
    print()
    
    all_checks_passed = True
    
    # Check core files
    print("1. CHECKING CORE FILES")
    print("-" * 70)
    
    core_files = [
        ("README.md", "Main documentation"),
        ("QUICKSTART.md", "Quick start guide"),
        ("sample_boq_data.csv", "Sample data"),
        ("data_transformation.py", "Transformation script"),
        ("powerbi_setup_guide.md", "Power BI guide"),
        ("dax_measures.txt", "DAX measures"),
        ("powerquery_m_script.txt", "Power Query script"),
        ("dashboard_mockup.md", "Dashboard mockup"),
        ("requirements.txt", "Python requirements"),
        (".gitignore", "Git ignore file"),
    ]
    
    for filepath, description in core_files:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    print()
    
    # Check generated files
    print("2. CHECKING GENERATED FILES (from data transformation)")
    print("-" * 70)
    
    generated_files = [
        ("boq_unpivoted.csv", "Unpivoted data"),
        ("lowest_bidder_per_item.csv", "Lowest bidder analysis"),
        ("item_variance_analysis.csv", "Variance analysis"),
        ("boq_analysis_report.txt", "Analysis report"),
    ]
    
    for filepath, description in generated_files:
        if not check_file_exists(filepath, description):
            print(f"  ℹ Run 'python data_transformation.py' to generate this file")
    
    print()
    
    # Validate data structure
    print("3. VALIDATING DATA STRUCTURE")
    print("-" * 70)
    
    if os.path.isfile("sample_boq_data.csv"):
        print("Sample BOQ Data:")
        expected_cols = ["Item_Code", "Description", "Unit", "Quantity", 
                        "Bidder_A", "Bidder_B", "Bidder_C", "Bidder_D"]
        if not validate_csv_structure("sample_boq_data.csv", expected_cols):
            all_checks_passed = False
    
    if os.path.isfile("boq_unpivoted.csv"):
        print("\nUnpivoted BOQ Data:")
        expected_cols = ["Item_Code", "Description", "Unit", "Quantity", 
                        "Bidder", "Unit_Rate", "Category", "Total_Amount"]
        if not validate_csv_structure("boq_unpivoted.csv", expected_cols):
            all_checks_passed = False
    
    print()
    
    # Check Python environment
    print("4. CHECKING PYTHON ENVIRONMENT")
    print("-" * 70)
    
    try:
        import pandas
        print(f"✓ pandas installed (version {pandas.__version__})")
    except ImportError:
        print("✗ pandas not installed - run: pip install pandas")
        all_checks_passed = False
    
    try:
        import numpy
        print(f"✓ numpy installed (version {numpy.__version__})")
    except ImportError:
        print("✗ numpy not installed - run: pip install numpy")
        all_checks_passed = False
    
    print()
    
    # Check data integrity
    print("5. CHECKING DATA INTEGRITY")
    print("-" * 70)
    
    if os.path.isfile("sample_boq_data.csv") and os.path.isfile("boq_unpivoted.csv"):
        try:
            import pandas as pd
            
            # Load data
            df_original = pd.read_csv("sample_boq_data.csv", dtype={'Item_Code': str})
            df_unpivoted = pd.read_csv("boq_unpivoted.csv", dtype={'Item_Code': str})
            
            # Check record counts
            bidder_cols = [col for col in df_original.columns if col.startswith('Bidder_')]
            expected_records = len(df_original) * len(bidder_cols)
            actual_records = len(df_unpivoted)
            
            if expected_records == actual_records:
                print(f"✓ Record count correct: {actual_records} records")
            else:
                print(f"✗ Record count mismatch: expected {expected_records}, got {actual_records}")
                all_checks_passed = False
            
            # Check categories
            categories = df_unpivoted['Category'].unique()
            if 'Other' in categories and len(categories) == 1:
                print("⚠ Warning: All items categorized as 'Other' - check Item_Code format")
            else:
                print(f"✓ Categories detected: {len(categories)} categories")
                for cat in sorted(categories):
                    count = len(df_unpivoted[df_unpivoted['Category'] == cat])
                    print(f"  - {cat}: {count} records")
            
            # Check for null values
            null_counts = df_unpivoted.isnull().sum()
            if null_counts.sum() == 0:
                print("✓ No null values found")
            else:
                print("⚠ Null values detected:")
                for col, count in null_counts[null_counts > 0].items():
                    print(f"  - {col}: {count} nulls")
            
        except Exception as e:
            print(f"✗ Error validating data: {e}")
            all_checks_passed = False
    
    print()
    
    # Final summary
    print("=" * 70)
    if all_checks_passed:
        print("✓ ALL VALIDATION CHECKS PASSED!")
        print()
        print("Your BOQ project is set up correctly. Next steps:")
        print("1. Review QUICKSTART.md for quick setup")
        print("2. Follow powerbi_setup_guide.md to create dashboard")
        print("3. Copy measures from dax_measures.txt into Power BI")
        return 0
    else:
        print("✗ SOME CHECKS FAILED")
        print()
        print("Please review the errors above and fix them.")
        print("Run 'python data_transformation.py' if files are missing.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
