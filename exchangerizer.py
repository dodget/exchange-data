import os
import requests

API_KEY = os.environ.get("API_KEY")


def get_url(from_currency, to_currency):
    return f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"


def get_data(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()["Realtime Currency Exchange Rate"]


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

    # build urls
    usd_to_yen_url = get_url("USD", "JPY")
    usd_to_dram_url = get_url("USD", "AMD")
    usd_to_kronner_url = get_url("USD", "DKK")

    # get the data
    usd_to_yen = get_data(usd_to_yen_url)
    usd_to_dram_url = get_data(usd_to_dram_url)
    usd_to_kronner_url = get_data(usd_to_kronner_url)

    # format the data
    exchange_data = build_output_data([usd_to_yen, usd_to_dram_url, usd_to_kronner_url])
    
    # write the data to a file
    write_file(exchange_data)

    return 0



if __name__ == "__main__":
    raise SystemExit(main())
