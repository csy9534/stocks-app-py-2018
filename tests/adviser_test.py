import json
import os
import pdb

from app.robo_adviser import parse_response

def test_parse_response():
    # setup:
    json_filepath = os.path.join(os.path.dirname(__file__), "example_responses/daily.json")
    with open(json_filepath, "r") as json_file: # h/t: https://stackoverflow.com/a/2835672/670433
        raw_response = json.load(json_file)

    # test:
    parsed_response = parse_response(raw_response)
    # I want this parsed response to be a list of dictionaries,
    # ... because I feel more comfortable writing that kind of data structure to a CSV file...
    assert parsed_response == [
        {"timestamp":"2018-06-08", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"},
        {"timestamp":"2018-06-07", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"},
        {"timestamp":"2018-06-06", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"},
        {"timestamp":"2018-06-05", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"},
        {"timestamp":"2018-06-04", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"},
        {"timestamp":"2018-06-01", "open":"todo", "high":"todo", "low":"todo", "close":"todo", "volume":"todo"}
    ]
