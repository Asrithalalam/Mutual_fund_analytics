import pandas as pd

#required data files for cleaning
nav_data = pd.read_csv("data/raw/02_nav_history.csv")
scheme_performance =pd.read_csv("data/raw/07_scheme_performance.csv")
investor_transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

# Display column names for each dataset
print("\nnav_data columns:",nav_data.columns.tolist())
print("\nscheme_performance columns:",scheme_performance.columns.tolist())
print("\ninvestor_transactions columns:",investor_transactions.columns.tolist())   

# Data Cleaning Steps for each file
#Dataset: 02_nav_history.csv
def clean_nav_data(nav_data):
    
    # Convert 'date' column to datetime format
    nav_data['date'] = pd.to_datetime(nav_data['date'], errors='coerce')
    
    #sort the data by 'amfi_code' and 'date'
    nav_data = nav_data.sort_values(by=['amfi_code', 'date'])
    
    #forward fill missing values in 'nav'
    nav_data['nav'] = nav_data.groupby('amfi_code')['nav'].ffill()
    
    #remove duplicates
    nav_data = nav_data.drop_duplicates()
    
    #validate NAV>0
    nav_data = nav_data[nav_data['nav'] > 0]
    
    #save cleaned nav_data to a new CSV file
    nav_data.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

    print("\nCleaned nav_data saved to data/processed/02_nav_history_cleaned.csv")
    
    return nav_data

#Dataset: 08_investor_transactions.csv
def clean_investor_transactions(investor_transactions):
    
    #date format
    investor_transactions['transaction_date'] = pd.to_datetime(investor_transactions['transaction_date'], errors='coerce')
    
    #standardize transaction type values
    investor_transactions['transaction_type'] = investor_transactions['transaction_type'].str.strip().str.title()
    mapping = {"Sip": "SIP", "Lumpsum": "Lumpsum", "Redemption": "Redemption"}
    investor_transactions['transaction_type'] = investor_transactions['transaction_type'].replace(mapping)
    
    #Amount validation(amount > 0): Ensure that the 'amount' column contains only positive values
    investor_transactions = investor_transactions[investor_transactions['amount_inr'] > 0]
    
    #KYC validation
    #standardize  KYC status values
    investor_transactions['kyc_status'] = investor_transactions['kyc_status'].str.strip().str.title().astype(str)
    
    #check unique values in 'kyc_status' column
    print("\nUnique values in 'kyc_status' column:", investor_transactions['kyc_status'].unique())    
    
    #allowed values for KYC status
    allowed_kyc_status = ['Verified', 'Pending', 'Rejected']
    
    #find rows with invalid KYC status
    invalid_kyc_rows = investor_transactions[~investor_transactions['kyc_status'].isin(allowed_kyc_status)]
    print(f"\nInvalid KYC records: {len(invalid_kyc_rows)}")

    if len(invalid_kyc_rows) > 0:
        print("\nRows with invalid KYC status:\n",invalid_kyc_rows)
        
    #save cleaned investor_transactions to a new CSV file
    investor_transactions.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)
    
    print("\nInvestor Transactions cleaned and saved to data/processed/08_investor_transactions_cleaned.csv")
    
    return investor_transactions

#Dataset: 07_scheme_performance.csv
def clean_scheme_performance(scheme_performance):
     
    #validate all return values are numeric
    return_columns = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct']
    
    for col in return_columns:
        scheme_performance[col] = pd.to_numeric(scheme_performance[col], errors='coerce')
        
    #flag anamolies
    scheme_performance['flag_anomaly'] = ((scheme_performance["return_1yr_pct"].abs() > 100)|(scheme_performance["return_3yr_pct"].abs() > 100)|(scheme_performance["return_5yr_pct"].abs() > 100))
    
    #expense ratio range
    scheme_performance['expense_ratio_valid'] = (scheme_performance['expense_ratio_pct'].between(0.1, 2.5))
    
    #save cleaned scheme_performance to a new CSV file
    scheme_performance.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)
    
    print("\nScheme Performance cleaned and saved to data/processed/07_scheme_performance_cleaned.csv")
    
    return scheme_performance

#cleaning remaining datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
aum_data = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip_inflows = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category_inflows = pd.read_csv("data/raw/05_category_inflows.csv")
folio_count = pd.read_csv("data/raw/06_industry_folio_count.csv")
portfolio_holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark_indices = pd.read_csv("data/raw/10_benchmark_indices.csv")

#Defining cleaning functions for the remaining datasets
#Dataset: 01_fund_master.csv
def clean_fund_master(fund_master):
    # Remove duplicate rows
    fund_master = fund_master.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    text_columns = ['fund_house', 'scheme_name', 'category',
                    'sub_category', 'plan', 'benchmark',
                    'fund_manager', 'risk_category',
                    'sebi_category_code']

    for column in text_columns:
        fund_master[column] = fund_master[column].str.strip()

    # Convert launch_date to datetime
    fund_master['launch_date'] = pd.to_datetime(
        fund_master['launch_date'],
        errors='coerce'
    )

    # Remove rows with missing AMFI code
    fund_master = fund_master.dropna(subset=['amfi_code'])

    # Remove duplicate AMFI codes
    fund_master = fund_master.drop_duplicates(subset='amfi_code')

    # Expense ratio validation
    fund_master = fund_master[
        (fund_master['expense_ratio_pct'] >= 0) &
        (fund_master['expense_ratio_pct'] <= 5)
    ]

    # Exit load validation
    fund_master = fund_master[
        fund_master['exit_load_pct'] >= 0
    ]

    fund_master.to_csv(
        "data/processed/01_fund_master_cleaned.csv",
        index=False
    )

    print("Fund Master cleaned successfully.")

    return fund_master

#Dataset: 03_aum_by_fund_house.csv
def clean_aum_by_fund_house(aum_data):

    # Remove duplicates
    aum_data = aum_data.drop_duplicates()

    # Date conversion
    aum_data['date'] = pd.to_datetime(
        aum_data['date'],
        errors='coerce'
    )

    # Remove spaces
    aum_data['fund_house'] = aum_data['fund_house'].str.strip()

    # Numeric conversion
    numeric_cols = [
        'aum_lakh_crore',
        'aum_crore',
        'num_schemes'
    ]

    for column in numeric_cols:
        aum_data[column] = pd.to_numeric(aum_data[column], errors='coerce')

    # Keep positive values only
    aum_data = aum_data[
        (aum_data['aum_crore'] > 0) &
        (aum_data['aum_lakh_crore'] > 0) &
        (aum_data['num_schemes'] > 0)
    ]

    aum_data.to_csv(
        "data/processed/03_aum_by_fund_house_cleaned.csv",
        index=False
    )

    print("AUM dataset cleaned successfully.")

    return aum_data

#Dataset: 04_monthly_sip_inflows.csv
def clean_monthly_sip_inflows(sip_inflows):

    # Remove duplicates
    sip_inflows = sip_inflows.drop_duplicates()

    # Convert month
    sip_inflows['month'] = pd.to_datetime(
        sip_inflows['month'],
        format='%Y-%m',
        errors='coerce'
    )

    # Convert numeric columns
    numeric_cols = [
        'sip_inflow_crore',
        'active_sip_accounts_crore',
        'new_sip_accounts_lakh',
        'sip_aum_lakh_crore',
        'yoy_growth_pct'
    ]

    for column in numeric_cols:
        sip_inflows[column] = pd.to_numeric(
            sip_inflows[column],
            errors='coerce'
        )

    # Validate positive values
    sip_inflows = sip_inflows[
        (sip_inflows['sip_inflow_crore'] >= 0) &
        (sip_inflows['active_sip_accounts_crore'] >= 0) &
        (sip_inflows['new_sip_accounts_lakh'] >= 0) &
        (sip_inflows['sip_aum_lakh_crore'] >= 0)
    ]

    sip_inflows = sip_inflows.sort_values('month')

    sip_inflows.to_csv(
        "data/processed/04_monthly_sip_inflows_cleaned.csv",
        index=False
    )

    print("Monthly SIP Inflows cleaned successfully.")

    return sip_inflows

#Dataset: 05_category_inflows.csv
def clean_category_inflows(category_inflows):

    # Remove duplicate rows
    category_inflows = category_inflows.drop_duplicates()

    # Convert month to datetime
    category_inflows['month'] = pd.to_datetime(
        category_inflows['month'],
        format='%Y-%m',
        errors='coerce'
    )

    # Remove leading/trailing spaces
    category_inflows['category'] = category_inflows['category'].str.strip()

    # Convert inflow to numeric
    category_inflows['net_inflow_crore'] = pd.to_numeric(
        category_inflows['net_inflow_crore'],
        errors='coerce'
    )

    # Keep valid inflows
    category_inflows = category_inflows[
        category_inflows['net_inflow_crore'].notnull()
    ]

    # Save cleaned dataset
    category_inflows.to_csv(
        "data/processed/05_category_inflows_cleaned.csv",
        index=False
    )

    print("Category Inflows cleaned successfully.")

    return category_inflows

#Dataset: 06_industry_folio_count.csv
def clean_industry_folio_count(folio_count):

    # Remove duplicate rows
    folio_count = folio_count.drop_duplicates()

    # Convert month
    folio_count['month'] = pd.to_datetime(
        folio_count['month'],
        format='%Y-%m',
        errors='coerce'
    )

    # Convert numeric columns
    numeric_cols = [
        'total_folios_crore',
        'equity_folios_crore',
        'debt_folios_crore',
        'hybrid_folios_crore',
        'others_folios_crore'
    ]

    for column in numeric_cols:
        folio_count[column] = pd.to_numeric(
            folio_count[column],
            errors='coerce'
        )

    # Keep positive values
    for column in numeric_cols:
        folio_count = folio_count[
            folio_count[column] >= 0
        ]

    # Save cleaned dataset
    folio_count.to_csv(
        "data/processed/06_industry_folio_count_cleaned.csv",
        index=False
    )

    print("Industry Folio Count cleaned successfully.")

    return folio_count

#Dataset: 09_portfolio_holdings.csv
def clean_portfolio_holdings(portfolio_holdings):

    # Remove duplicate rows
    portfolio_holdings = portfolio_holdings.drop_duplicates()

    # Convert portfolio date
    portfolio_holdings['portfolio_date'] = pd.to_datetime(
        portfolio_holdings['portfolio_date'],
        errors='coerce'
    )

    # Remove spaces
    text_cols = [
        'stock_symbol',
        'stock_name',
        'sector'
    ]

    for column in text_cols:
        portfolio_holdings[column] = portfolio_holdings[column].str.strip()

    # Convert numeric columns
    numeric_cols = [
        'weight_pct',
        'market_value_cr',
        'current_price_inr'
    ]

    for column in numeric_cols:
        portfolio_holdings[column] = pd.to_numeric(
            portfolio_holdings[column],
            errors='coerce'
        )

    # Weight validation
    portfolio_holdings = portfolio_holdings[
        (portfolio_holdings['weight_pct'] >= 0) &
        (portfolio_holdings['weight_pct'] <= 100)
    ]

    # Positive values
    portfolio_holdings = portfolio_holdings[
        (portfolio_holdings['market_value_cr'] >= 0) &
        (portfolio_holdings['current_price_inr'] > 0)
    ]

    # Sort
    portfolio_holdings = portfolio_holdings.sort_values(
        ['amfi_code', 'portfolio_date']
    )

    # Save cleaned dataset
    portfolio_holdings.to_csv(
        "data/processed/09_portfolio_holdings_cleaned.csv",
        index=False
    )

    print("Portfolio Holdings cleaned successfully.")

    return portfolio_holdings

#Dataset: 10_benchmark_indices.csv
def clean_benchmark_indices(benchmark_indices):

    # Remove duplicates
    benchmark_indices = benchmark_indices.drop_duplicates()

    # Convert date
    benchmark_indices['date'] = pd.to_datetime(
        benchmark_indices['date'],
        errors='coerce'
    )

    # Remove spaces
    benchmark_indices['index_name'] = benchmark_indices['index_name'].str.strip()

    # Convert close value
    benchmark_indices['close_value'] = pd.to_numeric(
        benchmark_indices['close_value'],
        errors='coerce'
    )

    # Positive values only
    benchmark_indices = benchmark_indices[
        benchmark_indices['close_value'] > 0
    ]

    benchmark_indices.to_csv(
        "data/processed/10_benchmark_indices_cleaned.csv",
        index=False
    )

    print("Benchmark Indices cleaned successfully.")

    return benchmark_indices


if __name__ == "__main__":
    # Clean each dataset
    cleaned_nav_data = clean_nav_data(nav_data)
    cleaned_investor_transactions = clean_investor_transactions(investor_transactions)
    cleaned_scheme_performance = clean_scheme_performance(scheme_performance)
    cleaned_fund_master = clean_fund_master(fund_master)
    cleaned_aum_by_fund_house = clean_aum_by_fund_house(aum_data)
    cleaned_monthly_sip_inflows = clean_monthly_sip_inflows(sip_inflows)
    cleaned_category_inflows = clean_category_inflows(category_inflows)
    cleaned_industry_folio_count = clean_industry_folio_count(folio_count)
    cleaned_portfolio_holdings = clean_portfolio_holdings(portfolio_holdings)
    cleaned_benchmark_indices = clean_benchmark_indices(benchmark_indices)
    