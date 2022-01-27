# Benutzt die Adafruit_IO API (Rest), um pseudo-zufällige Zahlen zu generieren
# Sorgt für einen realistischeren Verlauf, da immer nur 1°C Schritte möglich sind

from Adafruit_IO import Client, Feed, Data
import time as t
import random as r

USERNAME = 'user'
KEY = 'key'


def dirtyZufallsgenerator(ausgangswert):
    wert = r.randint(1, 4)
    print(wert)
    if wert == 1:
        ausgangswert += 1
    elif wert == 2:
        ausgangswert -= 1
    return ausgangswert


# alter_wert -= 1 if alter_wert > random_value else alter_wert + 1


aio = Client(USERNAME, KEY)
hauptwert = r.randint(-50, 50)

while True:
    while aio.receive('an-aus').value == "True":
        hauptwert = dirtyZufallsgenerator(hauptwert)
        print("Hauptwert:", hauptwert)

        aio.send('temperature', hauptwert)
        t.sleep(2)


