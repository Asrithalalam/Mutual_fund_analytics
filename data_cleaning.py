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

if __name__ == "__main__":
    # Clean each dataset
    cleaned_nav_data = clean_nav_data(nav_data)
    cleaned_investor_transactions = clean_investor_transactions(investor_transactions)
    cleaned_scheme_performance = clean_scheme_performance(scheme_performance)