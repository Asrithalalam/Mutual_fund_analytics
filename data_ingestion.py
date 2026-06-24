#import necessary libraries
import pandas as pd
import os
#store the path of the folder containing the CSV files
folder_path = "data/raw"
#get the list of files in the folder
files = os.listdir(folder_path)
print(f"Found {len(files)} files in the folder.") #count the number of files in the folder
for f in files:
    if f.endswith(".csv"): #check if the file is a CSV file
        print("\n" + "-" * 60)  #print a separator line for better readability -> '---------------'
        print(f"Processing file: {f}") #print the name of the file being processed
        file_path = os.path.join(folder_path, f) #get the full path of the file - "eg: data/raw/filename.csv" because pandas need the complete file location to read the file
        
        df=pd.read_csv(file_path) #read the CSV file into a pandas DataFrame
        print(f"Dataframe shape: {df.shape}") #print the shape of the DataFrame -> size of the DataFrame in terms of rows and columns
        print("\nColumns:" ,df.columns.tolist()) #print the list of column names in the DataFrame
        print("\nData types:",df.dtypes) #print the data types of each column in the DataFrame
        print("\nFirst 5 rows:",df.head())#print the first 5 rows of the DataFrame
        print("\nMissing values:\n",df.isnull().sum())  #print the number of missing values in each column of the DataFrame
        print("\nDuplicate rows:",df.duplicated().sum()) #print the number of duplicate rows in the 
        print()
#Exploring unique values in the specific file "01_fund_master.csv"
df=pd.read_csv("data/raw/01_fund_master.csv")
print("Unique fund houses:\n", df["fund_house"].unique()) #print the unique values in the "fund_house" column of the DataFrame
print("Unique categories:\n", df["category"].unique()) #print the unique values in the "category" column of the DataFrame   
print("Unique sub-categories:\n", df["sub_category"].unique()) #print the unique values in the "sub_category" column of the DataFrame
print("Unique risk categories:\n", df["risk_category"].unique()) #print the unique values in the "risk_category" column of the DataFrame

#Validating AMFI Codes
main = pd.read_csv("data/raw/01_fund_master.csv") #read the main CSV file into a pandas DataFrame
nav_file = pd.read_csv("data/raw/02_nav_history.csv") #read the NAV data CSV file into a pandas DataFrame
main_amfi_codes = set(main["amfi_code"]) #get the unique AMFI codes from the main DataFrame
nav_amfi_codes = set(nav_file["amfi_code"]) #get the unique AMFI
missing_amfi_codes =main_amfi_codes - nav_amfi_codes #find the AMFI codes that are present in the NAV data but not in the main data
print(f"Missing AMFI codes in NAV data: {missing_amfi_codes}") #print the missing AMFI codes