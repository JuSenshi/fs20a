# AUFGABE 1
# a) Message Queuing Telemetry Transport
# b) Der Broker ist ein Dienst, welcher den Datenaustausch zwischen Subscribern und Publishern betreibt
# c) temperature/roof und temperature/floor
# d) Client A sagt dem Broker Bescheid, dass er im Netz ist (CONNECT)
# d) Der Broker gibt die Bestätigung (CONN ACK)
# d) Client B sendet mit dem Retain Flag den Wert "25°C" im Topic temperature/roof zum Broker (PUBLISH)
# d) Client A abbonniert das Topic "temperature/roof"
# d) Wegen dem Retain-Flag sendet der Broker die Temperatur nun an Client A weiter (PUBLISH)
# d) Client A sendet die Temperatur "20°C" im Topic temperature/floor an den Broker (PUBLISH)
# d) Client B sendet die Temperatur "38°C" im Topic temperature/roof (PUBLISH)
# d) Der Broker sendet die Temperatur an die abonnierten Clients (Client A) weiter (PUBLISH)
# d) Der Client A sendet eine Disconnect-Nachricht an den Broker

# AUFGABE 2 a)
from Adafruit_IO import MQTTClient

Temperatur = 20  # GEGEBEN DURCH AUFGABENSTELLUNG

MQTT = MQTTClient('name', 'key')
MQTT.connect()
MQTT.publish('ds18b20', Temperatur)
MQTT.disconnect() # optional

# AUFGABE 2 b)
from Adafruit_IO import Client
import random as r

aio = Client('user', 'key')  # Könnte man theoretisch kürzen und in Zeile 31 mergen
random_value = r.randint(-50, 50)
aio.send('zufall', random_value)


# AUFGABE 3
# a) py -m http.server      # ALTERNATIV python / py3 oder so
# b)
import random as r
wert = r.randint(16, 36)

with open("index.html", "w") as datei:
    datei.write("""<html>
    <body>
    """ + wert + """ °C    
    </body>
    </html>
""")


# AUFGABE 4
<html>
<head>
<title>Temperatur-Watchdog</title>
</head>
<body>
<h1>Temperaturüberwachung im Serverraum</h1>
Die aktuelle <strong> Temperatur im <i>Serverraum 1</i> beträgt: 26.5°C <br>
<ul>
<li>Max. temp: 30.9°C</li>
<li>Avg. Temp: 27.0°C</li>
<li>Min. Temp: 24.1°C</li>
<img src="server.jpg">
</body>
</html>


# AUFGABE 5
# a)
import requests, re
html = requests.get("http://localhost:8000/drei.html")
temperaturen = []
pattern = r"\d+ °C"
for number in re.finditer(pattern, html.text):
    temperaturen.append(number.group().replace(" °C", ""))

print("Max:", max(temperaturen))
print("Min:", min(temperaturen))
print("Avg:", sum(temperaturen)/len(temperaturen))

# AUFGABE 5
# b)

for i in range(len(temperaturen)):
    if(temperaturen[i]) > 30:
        print('\033[91m', "Serverraum", i+1, ":", temperaturen[i], "°C", '\033[0m')