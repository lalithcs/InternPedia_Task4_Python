import requests

# Function to fetch live exchange rates from an API
def get_exchange_rates():
    try:
        # Using ExchangeRate-API (https://www.exchangerate-api.com/) for live exchange rates
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        data = response.json()
        rates = data['rates']
        return rates
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates:", e)
        return None

# Function to convert currency
def convert_currency(amount, source_currency, target_currency, rates):
    if source_currency in rates and target_currency in rates:
        source_rate = rates[source_currency]
        target_rate = rates[target_currency]
        converted_amount = amount / source_rate * target_rate
        return converted_amount
    else:
        return None

# Function to display the result
def display_result(amount, source_currency, target_currency, converted_amount):
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}\n")

# Main function
def main():
    print("Welcome to the Currency Converter Program!")

    # Fetch exchange rates
    rates = get_exchange_rates()
    if rates is None:
        return

    while True:
        print("Available currencies: USD, EUR, GBP, JPY, CAD, AUD")
        source_currency = input("Enter source currency: ").upper()
        target_currency = input("Enter target currency: ").upper()

        if source_currency == target_currency:
            print("Source and target currencies cannot be the same.\n")
            continue

        if source_currency not in rates or target_currency not in rates:
            print("Invalid currency selection. Please choose from the available currencies.\n")
            continue

        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")
            continue

        converted_amount = convert_currency(amount, source_currency, target_currency, rates)
        if converted_amount is not None:
            display_result(amount, source_currency, target_currency, converted_amount)
        else:
            print("Conversion failed. Please try again.\n")

        choice = input("Do you want to perform another conversion? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the Currency Converter Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
