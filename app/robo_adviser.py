from dotenv import load_dotenv
import json
import os
import requests
from IPython import embed

def parse_response(response_text):
    print(response_text)
    return [] #TODO: parse the response text and return a list of daily dictionaries





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
