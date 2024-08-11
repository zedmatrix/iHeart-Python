#!/usr/bin/env python3
import requests, functools, subprocess, argparse

# Define the API endpoint
url = "https://api.iheart.com/api/v2/content/liveStations/"

# Allow arguments to the search variable
parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('arg1', type=str, help='The first argument')
args = parser.parse_args()

print(f"Argument received: {args.arg1}")
# Send the GET request
search = args.arg1
response = requests.get(url + search)

# Check if the request was successful
if response.status_code == 200:

    data = response.json()
    keylist = list(data.keys())
    Dx = len(data)
    Dy = type(data)
    print(f"Data:  {Dx} == {Dy}")

    hits = data['hits']
    Hx = len(hits)
    Hy = type(hits)
    print(f"Hits: {Hx} // {Hy}")

    for i in range(Hx):
        mini_hits = hits[i]

        mini_id = mini_hits['id']
        mini_name = mini_hits['name']
        print(f"Station: {mini_id} {mini_name} \nStreams:")
        streams = mini_hits['streams']

        for key,value in streams.items():
            print(f"{key} URL: {value}")

else:
    print(f"Error: {response.status_code}")
