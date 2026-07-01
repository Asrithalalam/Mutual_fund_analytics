# Mutual Fund Analytics Capstone Project

## Project Overview

This project is a Mutual Fund Analytics Capstone Project focused on building a complete data analytics pipeline for the Indian Mutual Fund industry.

The project includes:

- Data ingestion from CSV datasets
- Live NAV data collection using MFAPI
- Data quality validation
- Data cleaning and transformation
- Exploratory Data Analysis (EDA)
- SQL-based analysis
- Dashboard development
- Business insights and reporting

---

## Project Structure

```text
MUTUAL_FUND_ANALYTICS
│
├── data/
│   ├── raw/
│   └── processed/
├── EDA_charts/
├── notebooks/
├── database/
├── sql/
├── dashboard/
├── reports/
│
├── data_ingestion.py
├── data_cleaning.py
├── database.py
├── live_nav_fetch.py
├── requirements.txt
├── data_dictionary.md
├── README.md
```

---

## Datasets

The project uses the following datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Day 1 Deliverables

### Project Setup

- Created project folder structure
- Initialized Git repository
- Connected project to GitHub

### Data Ingestion

- Loaded all 10 datasets using Pandas
- Displayed dataset shapes
- Inspected column names
- Verified data types
- Displayed sample records

### Data Quality Checks

- Checked missing values
- Checked duplicate records
- Validated AMFI codes across datasets

### Fund Exploration

- Identified unique fund houses
- Analyzed categories and sub-categories
- Examined risk classifications

### Live NAV Data Collection

- Connected to MFAPI
- Parsed JSON responses
- Converted API data into Pandas DataFrames
- Saved NAV history as CSV files

---

## Key Findings

- Successfully loaded all datasets.
- No duplicate records found.
- All AMFI codes in `fund_master` exist in `nav_history`.
- Missing values were found only in `yoy_growth_pct` within `monthly_sip_inflows.csv`.
- Dataset contains 10 mutual fund houses.
- Dataset includes Equity and Debt categories with multiple sub-categories and risk levels.

---

## Day 2 Deliverables

### Data Cleaning & Preprocessing

- Cleaned all raw datasets and created processed versions.
- Standardized column names across datasets.
- Converted date columns to proper datetime format.
- Removed duplicate records.
- Handled missing values using appropriate techniques.
- Corrected inconsistent data types.
- Standardized categorical values.
- Validated AMFI codes across related datasets.
- Created derived columns where required (e.g., year from date).
- Saved cleaned datasets into the `processed` folder.

### Processed Datasets

- 01_fund_master_cleaned.csv
- 02_nav_history_cleaned.csv
- 03_aum_history_cleaned.csv
- 04_monthly_sip_inflows_cleaned.csv
- 05_category_inflows_cleaned.csv
- 06_industry_folio_count_cleaned.csv
- 07_scheme_performance_cleaned.csv
- 08_investor_transactions_cleaned.csv
- 09_portfolio_holdings_cleaned.csv
- 10_benchmark_indices_cleaned.csv

### Key Outcomes

- Improved data consistency across datasets.
- Removed invalid and duplicate records.
- Prepared datasets for visualization and analysis.
- Established a clean data pipeline for downstream EDA and SQL analysis.

---
## Day 3 Deliverables

### Exploratory Data Analysis (EDA)

Created multiple visualizations to analyze trends, fund performance, investor activity, and portfolio allocation.

### Visualizations Created

1. Daily NAV Trend Analysis (Plotly)
2. AUM Growth by Fund House (Seaborn)
3. Monthly SIP Inflow Trend (Plotly)
4. Category-wise Net Inflow Heatmap (Seaborn)
5. Mutual Fund Folio Count Growth
6. NAV Return Correlation Matrix
7. Sector Allocation Donut Chart

### Key EDA Insights

- Daily NAVs showed an overall upward trend across most schemes.
- AUM increased consistently across major fund houses.
- Monthly SIP inflows demonstrated sustained growth over the analysis period.
- Equity-oriented categories attracted comparatively higher inflows.
- Mutual fund folios increased steadily, indicating growing retail participation.
- Daily NAV returns of several equity schemes showed strong positive correlations.
- Financial Services and Information Technology represented significant portions of portfolio allocations.

---
## Technologies Used

- Python
- Pandas
- NumPy
- Requests
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- Jupyter Notebook
- Git
- GitHub

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Directory

```bash
cd mutual-fund-analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Project Workflow

```text
CSV Datasets
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Processed Datasets
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
SQL Analysis
      │
      ▼
Dashboard Development
      │
      ▼
Business Insights & Reporting
```

## EDA Charts Generated

The following charts were generated and exported as PNG files:

- NAV Trend Analysis
- AUM Growth by Fund House
- Monthly SIP Inflow Trend
- Category Inflow Heatmap
- Folio Count Growth
- NAV Return Correlation Matrix
- Sector Allocation Donut Chart

All charts are stored in the `EDA_charts/` directory.

---

## Future Work

- SQL-based analytical queries
- Dashboard development using Power BI
- Advanced business insights
- Performance benchmarking against market indices
- Portfolio performance analytics
- Interactive reporting and visualization

---

## Author

**Asritha Lalam**

Mutual Fund Analytics Capstone Project