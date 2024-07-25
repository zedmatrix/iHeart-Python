import requests, functools, subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QPushButton
)

app = QApplication([])

def click(value):
    print(f"Stream: {value}")
    stream = f"{value}"
    mpv = subprocess.Popen(["mpv", stream])
    returncode = mpv.wait()

#mpv = subprocess.Popen(["mpv", "--volume=50"], stream)
# Define the API endpoint
url = "https://api.iheart.com/api/v2/content/liveStations/"

# Send the GET request
#Oldies 5110
#Leo 1360 KMJM
search = '4744'
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
    vlayout = QVBoxLayout()
    for i in range(Hx):
        mini_hits = hits[i]

        mini_id = mini_hits['id']
        mini_name = mini_hits['name']
        print(f"{mini_id} {mini_name}")
        streams = mini_hits['streams']

        for key,value in streams.items():
            hlayout = QHBoxLayout()
            hlabel = QLabel( f"{key}" )
            hlabel.setFixedWidth(100)

            hbutton = QPushButton( f"{value}" )
            hbutton.setFixedWidth(300)
            hbutton.clicked.connect(functools.partial(click, value))
            hlayout.addWidget( hlabel )
            hlayout.addWidget( hbutton )
            vlayout.addLayout(hlayout)

        widget = QWidget()
        widget.setWindowTitle(f'{mini_id} {mini_name}')
        widget.setFixedSize(600, 300)
        widget.setLayout(vlayout)
        widget.show()
        app.exec()

else:
    print(f"Error: {response.status_code}")
