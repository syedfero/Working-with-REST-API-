import pandas as pd
import requests
def fetch_data(self):
    response = requests.get("<https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json>")
    data = response.json()  # Converts JSON response to a Python dictionary
    df = pd.DataFrame(data)  # Converts dictionary to pandas DataFrame
    df.to_csv('instruments.csv', index=False)  # Save DataFrame to CSV
def get_info_by_symbol(self, symbol):
    df = pd.read_csv('instruments.csv')  # Load data from CSV
    filtered_df = df[df['symbol'] == symbol]  # Filter rows
    if not filtered_df.empty:
        return filtered_df.iloc[0]  # Return the first row of the filtered DataFrame
    return None  # Return None if no matching symbol is found
