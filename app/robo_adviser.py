import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests

def parse_response(response_text):
    if isinstance(response_text, str):
        response_text = json.loads(response_text)

    results = []
    time_series_daily = response_text["Time Series (Daily)"]
    for trading_date in time_series_daily:
        prices = time_series_daily[trading_date]
        result = {
            "date": trading_date,
            "open": prices["1. open"],
            "high": prices["2. high"],
            "low": prices["3. low"],
            "close": prices["4. close"],
            "volume": prices["5. volume"]
        }
        results.append(result)
    return results

def write_prices_to_file(prices=[], filename="db/prices.csv"):
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", filename)
    with open(csv_filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        for d in prices:
            row = {
                "timestamp": d["date"],
                "open": d["open"],
                "high": d["high"],
                "low": d["low"],
                "close": d["close"],
                "volume": d["volume"]
            }
            writer.writerow(row)

if __name__ == '__main__':

    load_dotenv()
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."
    menu = """
    ------------------------
    Welcome to ROBO STOCK
    ------------------------
    """
    print(menu)
    symbol = input("Please input a stock symbol (e.g. 'NFLX'): ")

    try:
        float(symbol)
        quit("CHECK YOUR SYMBOL. EXPECTING NON-NUMERIC SYMBOL")

    except ValueError as e:
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
        response = requests.get(request_url)

    if "Error Message" in response.text:
        print("REQUEST ERROR, PLEASE TRY AGAIN. CHECK STOCK SYMBOL")
        quit("STOPPING THE PROGRAM")

    daily_prices = parse_response(response.text)

    write_prices_to_file(prices=daily_prices, filename="db/prices.csv")

    latest_price = daily_prices[0]["close"]
    latest_price = float(latest_price)

    high_prices = [float(prices["high"]) for prices in daily_prices]
    avg_high_prices = sum(high_prices)/len(high_prices)

    low_prices = [float(prices["low"]) for prices in daily_prices]
    avg_low_prices = sum(low_prices)/len(low_prices)

    latest_price_usd = "${0:,.2f}".format(latest_price)
    high_prices_usd = "${0:,.2f}".format(avg_high_prices)
    low_prices_usd = "${0:,.2f}".format(avg_low_prices)

print("Latest Closing Price: " + latest_price_usd)
print("Recent Average Highest Price: " + high_prices_usd)
print("Recent Average Lowest Price: " + low_prices_usd)

if latest_price_usd > high_prices_usd:
    print("GOOD TO SELL!")
if latest_price_usd < low_prices_usd:
    print("GOOD TO BUY!")
if low_prices_usd < latest_price_usd < high_prices_usd:
    print("TIME TO HOLD!")
