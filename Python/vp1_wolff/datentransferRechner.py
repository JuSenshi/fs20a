from datetime import datetime
from datetime import time
import os

dateigroesse = float(input("Bitte geben Sie die Dateigröße in MiB ein: "))
uebertragungsgeschwindigkeit = float(input("Bitte geben Sie die Übertragungsgeschwindigkeit in Mbit/s ein: "))

geschwindigkeit_in_mibs = ((uebertragungsgeschwindigkeit * 10 ** 6) / 8) / 2 ** 20

gesamtzeit_in_sek = dateigroesse/geschwindigkeit_in_mibs

stunden = int(gesamtzeit_in_sek / 3600)
minuten = int(gesamtzeit_in_sek / 60)
sekunden = int(gesamtzeit_in_sek - minuten*60)
millis = int((gesamtzeit_in_sek - minuten*60 - sekunden)*1000000)

downloadzeit = time(stunden, minuten, sekunden, millis)

print("Ihre Datentransferraten: ")
print('{:>10} {:<10}'.format(round(geschwindigkeit_in_mibs, 2), "MiB/s"))
print('{:>10} {:<10}'.format(round(geschwindigkeit_in_mibs * 60, 2), "MiB/min"))
print("\nDer Download dieser Datei dauert")
print(downloadzeit)
