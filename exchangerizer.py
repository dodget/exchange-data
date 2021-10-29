import os
import requests

API_KEY = os.environ.get("API_KEY")

CURRENCIES = [
    ("USD", "JPY"),
    ("USD", "AMD"),
    ("USD", "DKK")
]


def get_url(from_currency, to_currency):
    return f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"


def get_data(currency_codes):
    data = []
    for code in currency_codes:
        r = requests.get(get_url(code[0], code[1]))
        r.raise_for_status()
        data.append(r.json()["Realtime Currency Exchange Rate"])
    return data


def build_output_data(list_of_exchanges):
    return [
        {
            "from": exchange["2. From_Currency Name"],
            "to": exchange["4. To_Currency Name"],
            "exchange": float(exchange["5. Exchange Rate"])
        }
        for exchange in list_of_exchanges
    ]


def write_file(exchange_data):
    with open("rates.txt", "w") as file:
        for exchange in exchange_data:
            file.write(f"{exchange['from']} yields {exchange['exchange']} {exchange['to']}\n")
    

def main():

    # get the data
    data = get_data(CURRENCIES)

    # format the data
    exchange_data = build_output_data(data)
    
    # write the data to a file
    write_file(exchange_data)

    return 0



if __name__ == "__main__":
    raise SystemExit(main())
