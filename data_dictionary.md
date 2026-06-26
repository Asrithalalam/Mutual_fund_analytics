# Data Dictionary

## Project
Mutual Fund Analytics Platform

---

# dim_fund

**Source:** 01_fund_master.csv

| Column Name | Data Type | Business Definition |
|------------|------------|---------------------|
| amfi_code | INTEGER | Unique AMFI identifier for a mutual fund scheme |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| risk_category | TEXT | Risk classification of the fund |

---

# fact_nav

**Source:** 02_nav_history_cleaned.csv

| Column Name | Data Type | Business Definition |
|------------|------------|---------------------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value of the scheme on a specific date |

---

# fact_transactions

**Source:** 08_investor_transactions_cleaned.csv

| Column Name | Data Type | Business Definition |
|------------|------------|---------------------|
| investor_id | INTEGER | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification of city |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | KYC verification status |

---

# fact_performance

**Source:** 07_scheme_performance_cleaned.csv

| Column Name | Data Type | Business Definition |
|------------|------------|---------------------|
| amfi_code | INTEGER | Fund identifier |
| scheme_name | TEXT | Name of mutual fund scheme |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| plan | TEXT | Growth/Direct/Regular plan |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Benchmark return over 3 years |
| alpha | REAL | Alpha measure |
| beta | REAL | Beta measure |
| sharpe_ratio | REAL | Risk-adjusted return metric |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown percentage |
| aum_crore | REAL | Assets Under Management (crores) |
| expense_ratio_pct | REAL | Expense ratio percentage |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade assigned |
| anomaly_flag | BOOLEAN | Indicates abnormal return values |
| expense_ratio_valid | BOOLEAN | Indicates valid expense ratio range |

---

# fact_aum

**Source:** 03_aum_by_fund_house.csv

| Column Name | Data Type | Business Definition |
|------------|------------|---------------------|
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| aum | REAL | Assets Under Management |
| reporting_date | DATE | AUM reporting date |

---

# Data Quality Checks Performed

## NAV Data
- Parsed date column to datetime
- Sorted by AMFI code and date
- Forward-filled missing NAV values
- Removed duplicate records
- Validated NAV > 0

## Investor Transactions
- Standardized transaction types
- Validated amount > 0
- Converted transaction dates
- Validated KYC status values

## Scheme Performance
- Converted returns to numeric
- Flagged anomalous return values
- Validated expense ratio range (0.1% - 2.5%)

---

# Database

Database Name: `bluestock_mf.db`

Schema Type: Star Schema

Dimension Tables:
- dim_fund
- dim_date

Fact Tables:
- fact_nav
- fact_transactions
- fact_performance
- fact_aum