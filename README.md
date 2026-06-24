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
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
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
Extract
│
├── CSV Datasets
└── MFAPI Data

Transform
│
├── Data Validation
├── Data Cleaning
└── Quality Checks

Load
│
├── Processed Data
├── SQL Analysis
└── Dashboards
```

---

## Future Work

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- SQL Queries and Analysis
- Dashboard Development
- Performance Benchmarking
- Business Insights Generation

---

## Author

**Asritha Lalam**

Mutual Fund Analytics Capstone Project