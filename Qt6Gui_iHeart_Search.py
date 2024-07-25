import urllib, requests, json, argparse
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication([])
url = "http://api2.iheart.com/api/v1/catalog/searchAll?"
#url = "https://api.iheart.com/api/v2/content/liveStations?"

search = "60s+70s"
parameters = (
    f'&keywords={search}'+
    '?&max=5'+
    '?&genre=rock'+
    '?&stations=live'
    )

response = urllib.request.urlopen(url + parameters)

assert (response.getheader ('Content-Type').casefold () == 'application/json;charset=UTF-8'.casefold ())

results = json.loads (response.read ().decode ("utf-8"))

if (results['errors']):
    print(results['errors'])
else:
    keylist = list(results.keys())
    Rx = len(results)
    Ry = type(results)
    print(f"Length: {Rx} // Type: {Ry}")
    print(f"Keys: {keylist} ")
    print("======================\n")
    for i in keylist:
        R_type = type(results[i])
        if results[i] is list:
            R_len = len(results[i])
        else:
            R_len = 0

        print(f"Key: {i} ,Length: {R_len} ,Type: {R_type}")

    artists = results['artists']
    Ax = len(artists)
    Ay = type(artists)
    print(f"Artists: Length: {Ax} // Type: {Ay}")

    print("======================\n")
    stations = results['stations']
    Sx = len(stations)
    Sy = type(stations)
    print(f"Stations: Length: {Sx} // Type: {Sy}")
# output the station list to a Qt V-H Box Layout Window
    vlayout = QVBoxLayout()

    for i in range(Sx):
        mini = stations[i]
        hlayout = QHBoxLayout()

        mini_id = QPushButton( f"{mini['id']}" )
        mini_id.setFixedWidth(50)
        hlayout.addWidget( mini_id )

        mini_name = QLabel( f"{mini['name']}" )
        mini_name.setFixedWidth(150)
        hlayout.addWidget( mini_name )

        mini_desc = QLabel( f"{mini['description']}" )
        mini_desc.setFixedWidth(300)
        hlayout.addWidget( mini_desc )
        vlayout.addLayout(hlayout)

    widget = QWidget()
    widget.setFixedSize(600, 300)
    widget.setLayout(vlayout)
    widget.show()
    app.exec()
