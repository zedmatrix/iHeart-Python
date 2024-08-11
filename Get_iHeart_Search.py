#!/usr/bin/env python3
import urllib, requests, json, argparse

def print_keylist():
    for i in keylist:
        R_type = type(results[i])
        if results[i] is list:
            R_len = len(results[i])
        else:
            R_len = 0
        print(f"Key: {i} ,Length: {R_len} ,Type: {R_type}")

parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('arg1', type=str, help='The first argument')
args = parser.parse_args()

print(f"Argument received: {args.arg1}")

url = "http://api2.iheart.com/api/v1/catalog/searchAll"
#search = "60s+70s"
search = args.arg1
parameters = (
    f'?&keywords={search}'
    )

response = urllib.request.urlopen(url + parameters)

assert (response.getheader ('Content-Type').casefold () == 'application/json;charset=UTF-8'.casefold ())

results = json.loads (response.read ().decode ("utf-8"))

if (results['errors']):
    print(f"Error: {results}")
else:
    keylist = list(results.keys())
    Rx = len(results)
    Ry = type(results)
    print(f"Length: {Rx} // Type: {Ry}")
    print(f"Keys: {keylist} ")
    print("======================\n")
    artists = results['artists']
    Ax = len(artists)
    Ay = type(artists)
    print(f"Artists: Length: {Ax} // Type: {Ay}")
    #print(f"{artists}")
    print("======================\n")
    tracks = results['tracks']
    Tx = len(tracks)
    Ty = type(tracks)
    print(f"Tracks: Length: {Tx} // Type: {Ty}")
    #print(tracks)
    #for i in range(Tx):
    #    mini = tracks[i]
    #    title = f"{mini['title']}"
    #    artist = f"{mini['artist']}"
    #    album = f"{mini['album']}"
    #    stream = f'{mini['streamReady']}'
    #    preview = f'{mini['previewPath']}'
        #print(f'{stream}:{title} - {artist} - {album}')
    #    print(f'{stream}:{title} - {preview}')
    #print("======================\n")

    stations = results['stations']
    Sx = len(stations)
    Sy = type(stations)
    print(f"Stations: Length: {Sx} // Type: {Sy}")
    print("======================\n")

    for i in range(Sx):
        mini = stations[i]

        mini_id = f"{mini['id']}"
        mini_name = f"{mini['name']}"
        mini_desc = f"{mini['description']}"
        print(mini_id, mini_name, mini_desc)
