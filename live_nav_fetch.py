# Import the requests(used to communicate with websites and APIs) library for making HTTP requests
import requests
import pandas as pd

url= "https://api.mfapi.in/mf/125497" #url of the API endpoint to fetch data for a specific mutual fund scheme  
response = requests.get(url) # Make a GET request to the API endpoint
data = response.json() # Parse the JSON response
print("Scheme Name:", data["meta"]["scheme_name"]) # Print the scheme name from the response

nav_df = pd.DataFrame(data["data"]) # Convert the 'data' part of the response into a pandas DataFrame
print(nav_df.head()) # Print the first 5 rows of the DataFrame

#convert to csv
nav_df.to_csv("data/raw/hdfc_top100_live_nav.csv", index=False) # Save the DataFrame to csv file in the specified path without the index column
print("CSV file saved successfully..") # Print a success message
print()
#fetching NAV for 5 key schemes
print("Fetching NAV for 5 key schemes")

schemes = {
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_large_cap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

for scheme_code, scheme_name in schemes.items():

    print(f"\nFetching {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    print("Scheme Name:", data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{scheme_name}_nav.csv",
        index=False
    )

    print(f"Saved {scheme_name}_nav.csv")