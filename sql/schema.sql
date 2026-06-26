CREATE TABLE dim_fund(
    fund_id INTEGER primary key,
    amfi_code INTEGER unique,
    fund_name text,
    category text,
    fund_house text);

CREATE TABLE dim_date(
    date_id INTEGER primary key,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    quarter INTEGER);

CREATE TABLE fact_nav(
    nav_id INTEGER primary key,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id));    

CREATE TABLE fact_transactions(
    transaction_id INTEGER primary key,
    fund_id INTEGER,
    date_id INTEGER,
    investor_id INTEGER,
    amount_inr REAL,
    transaction_type TEXT,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id));

CREATE TABLE fact_performance(
    performance_id INTEGER primary key,
    fund_id INTEGER,
    return_1y_pct REAL,
    return_3y_pct REAL, 
    return_5y_pct REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id));

CREATE TABLE fact_aum(
    aum_id INTEGER primary key,
    fund_id INTEGER,
    date_id INTEGER,
    aum REAL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id));