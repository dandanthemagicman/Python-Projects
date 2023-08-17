#Currency Converter
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        
        if target_currency in rates:
            return rates[target_currency]
        else:
            raise ValueError("Target currency not found in exchange rates.")
    else:
        raise ValueError("Failed to fetch exchange rates.")

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

# Example usage
amount_to_convert = float(input("Enter the amount to convert: "))
base_currency = input("Enter the base currency (e.g., USD): ").upper()
target_currency = input("Enter the target currency (e.g., EUR): ").upper()

try:
    converted_amount = convert_currency(amount_to_convert, base_currency, target_currency)
    print(f"{amount_to_convert} {base_currency} is approximately {converted_amount:.2f} {target_currency}")
except ValueError:
    print("Error: An error occurred during the currency conversion.")
