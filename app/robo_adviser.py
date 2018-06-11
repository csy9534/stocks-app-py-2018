from dotenv import load_dotenv
import json
import os
import requests
import pdb

def parse_response(response_text):
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





if __name__ == '__main__': # only execute if file invoked from the command-line, not when imported into other files, like tests

    # ASSEMBLE REQUEST URL
    # ... see: https://www.alphavantage.co/support/#api-key

    load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."
    symbol = "NFLX" # input("Please input a stock symbol (e.g. 'NFLX'): ")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    print(request_url)

    # ISSUE GET REQUEST

    response = requests.get(request_url)

    # PARSE RESPONSE

    daily_prices = parse_response(response.text)

    # WRITE TO CSV

    # CALCULATE LATEST PRICE

    #latest_price_usd = "$100,000.00"
    #print(f"LATEST DAILY CLOSING PRICE FOR {symbol} IS: {latest_price_usd}")
