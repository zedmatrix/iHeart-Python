import requests, functools, subprocess

# Define the API endpoint
url = "https://api.iheart.com/api/v2/content/liveStations/"

# Send the GET request
search = '5235'
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
