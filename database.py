#install dependency - pip install sqlalchemy -->if needed

import pandas as pd
from sqlalchemy import create_engine, text

# Create SQLite Database Connection

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

print("Connected to SQLite database.")

# Read Cleaned CSV Files

nav_data = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

investor_transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

scheme_performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# If required for project use:

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

aum_data = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# Load Data into SQLite

fund_master.to_sql(
    "dim_fund",
    con=engine,
    if_exists="replace",
    index=False
)

nav_data.to_sql(
    "fact_nav",
    con=engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "fact_transactions",
    con=engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "fact_performance",
    con=engine,
    if_exists="replace",
    index=False
)

aum_data.to_sql(
    "fact_aum",
    con=engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded successfully.")

# Verifying Row Counts
tables = {
    "dim_fund": fund_master,
    "fact_nav": nav_data,
    "fact_transactions": investor_transactions,
    "fact_performance": scheme_performance,
    "fact_aum": aum_data
}

print("\nRow Count Verification")
print("-" * 50)

with engine.connect() as connection:

    for table_name, dataframe in tables.items():

        source_rows = len(dataframe)

        target_rows = connection.execute(
            text(f"SELECT COUNT(*) FROM {table_name}")
        ).scalar()

        print(
            f"{table_name:<20} "
            f"Source: {source_rows:<10} "
            f"Target: {target_rows}"
        )

print("\nDatabase loading completed successfully.")