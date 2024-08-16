from polygon import RESTClient
from typing import cast # needed to cast HTTPResponse as JSON
from urllib3 import HTTPResponse
import config # config.py to get API_KEY
import json   # because polygon returns the data from the API call in HTTPResponse format


client = RESTClient(config.API_KEY)

# Get NVDA ticket data
aggs = cast(
    HTTPResponse,
    client.get_aggs('NVDA', 1, 'day', '2023-01-09', '2023-02-10', raw=True)
)

data = json.loads(aggs.data)

# Print specific data by looping through the JSON object
for item in data:
    if item == 'results':
        resultsData = data[item]

for bar in resultsData:
    print(bar)