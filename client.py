from polygon import RESTClient
from typing import cast # needed to cast HTTPResponse as JSON
from urllib3 import HTTPResponse
import config # config.py to get API_KEY
import json   # because polygon returns the data from the API call in HTTPResponse format
from plotly import graph_objects as go
import pandas as pd


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


# Capture data for graphing
closeList = []
openList = []
highList = []
lowList = []
timeList = []
for bar in resultsData:
    for category in bar:
        if category == 'c':
            closeList.append(bar[category])
        elif category == 'o':
            openList.append(bar[category])
        elif category == 'h':
            highList.append(bar[category])
        elif category == 'l':
            lowList.append(bar[category])
        elif category == 't':
            timeList.append(bar[category])

# Convert timestamp
times = []
for time in timeList:
    times.append(pd.Timestamp(time, tz='GMT', unit='ms'))

# Plot NVDA data (more info: https://plotly.com/python/candlestick-charts/)
fig = go.Figure()
fig.add_trace(go.Candlestick(x=times, open=openList, close=closeList, high=highList, low=lowList, name='NVDA Monthly 2023'))
fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
fig.show() #opens a browser with the plotly stock graph (so cool)