import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests

def parse_response(response_text):
    # response_text can be either a raw JSON string or an already-converted dictionary
    if isinstance(response_text, str): # if not yet converted, then:
        response_text = json.loads(response_text) # convert string to dictionary

    results = []
    time_series_daily = response_text["Time Series (Daily)"] #> a nested dictionary
    for trading_date in time_series_daily: # FYI: can loop through a dictionary's top-level keys/attributes
        prices = time_series_daily[trading_date] #> {'1. open': '101.0924', '2. high': '101.9500', '3. low': '100.5400', '4. close': '101.6300', '5. volume': '22165128'}
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
                "timestamp": d["date"], # change attribute name to match project requirements
                "open": d["open"],
                "high": d["high"],
                "low": d["low"],
                "close": d["close"],
                "volume": d["volume"]
            }
            writer.writerow(row)





if __name__ == '__main__': # only execute if file invoked from the command-line, not when imported into other files, like tests

    load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

    api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

    # CAPTURE USER INPUTS (SYMBOL)

    symbol = "NFLX" # input("Please input a stock symbol (e.g. 'NFLX'): ")

    # VALIDATE SYMBOL AND PREVENT UNECESSARY REQUESTS
    # ... todo

    # ASSEMBLE REQUEST URL
    # ... see: https://www.alphavantage.co/support/#api-key

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    # ISSUE "GET" REQUEST

    response = requests.get(request_url)

    # VALIDATE RESPONSE AND HANDLE ERRORS
    # ... todo

    # PARSE RESPONSE (AS LONG AS THERE ARE NO ERRORS)

    daily_prices = parse_response(response.text)

    # WRITE TO CSV

    write_prices_to_file(prices=daily_prices, filename="db/prices.csv")

    # PERFORM CALCULATIONS
    # ... todo (HINT: use the daily_prices variable, and don't worry about the CSV file anymore :-)

    # PRODUCE FINAL RECOMMENDATION
    # ... todo
