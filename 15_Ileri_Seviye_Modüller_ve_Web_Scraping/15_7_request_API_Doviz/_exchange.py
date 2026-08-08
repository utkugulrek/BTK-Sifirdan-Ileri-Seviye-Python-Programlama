import json
import requests

API_KEY = "api_key"  # Replace with your actual API key
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

sourceCurrency = input("Enter the source currency (e.g., USD): ").upper()
targetCurrency = input("Enter the target currency (e.g., EUR): ").upper()

amount = float(input(f"Enter the amount in {sourceCurrency}: "))

response = requests.get(API_URL + sourceCurrency, timeout=10)
response_data = response.json()

print(
    f"1 {sourceCurrency} = {response_data['conversion_rates'][targetCurrency]} {targetCurrency}"
)
print(
    f"Amount in {targetCurrency}: {amount * response_data['conversion_rates'][targetCurrency]}"
)
