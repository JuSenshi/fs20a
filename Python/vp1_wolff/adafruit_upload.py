from Adafruit_IO import Client, Feed, Data
import time as t
import random as r

USERNAME = 'Ju_Senshi'
KEY = 'aio_ZHsJ90asWJEWxnSzvUuGiwM4Gt5m'


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


