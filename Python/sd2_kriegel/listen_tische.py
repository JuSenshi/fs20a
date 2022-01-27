# Übungsaufgabe zum EVA-Prinzip und der Nutzung von Listen anhand des Beispiels
# einer Tisch-Verwaltung in einem Restaurant
# Styleguide: https://google.github.io/styleguide/pyguide.html
# -----------------------------------------------------------

tischliste = [2, 0, 4, 0, 3, 4, 4, 0, 0, 2, 2, 3, 0, 4, 2]
freie_tische = []


def getFreieTische():
    freie_tische.clear()
    for index, value in enumerate(tischliste):
        if value == 0:
            freie_tische.append(index)


def printTischListe():
    for index, value in enumerate(tischliste):
        print("Tisch ", index, ": ", value, sep="")


def printFreieTische():
    getFreieTische()
    for i in freie_tische:
        print("Tisch", i, "ist frei.")


def tischReservieren():
    # Reservierungen
    print("Diese Tische stehen derzeit zur Verfügung: ")
    printFreieTische()
    tischwahl = input("Bitte wählen Sie einen Tisch: ")
    if tischwahl.isnumeric() and int(tischwahl) in freie_tische:
        tischwahl = int(tischwahl)
        personen = input("Wie viele Personen? ")

        if personen.isnumeric():
            tischliste[tischwahl] = personen
            print("Tisch", tischwahl, "wurde für", personen, "Personen reserviert.")
    else:
        print("Dies war keine korrekte Eingabe.")


def reservierungLoeschen():
    reservierterTisch = input("Bitte geben Sie die Tischnummer Ihrer Reservierung ein: ")

    if reservierterTisch.isnumeric() and tischliste[int(reservierterTisch)] != 0:
        reservierterTisch = int(reservierterTisch)
        tischliste[reservierterTisch] = 0
        print("Die Reservierung wurde erfolgreich gelöscht.")
    else:
        print("Dies war keine korrekte Eingabe.")


########################################################################################################################

wahl = ""

while wahl != "E":
    print("\nWas möchten Sie tun?")
    print("[R]: Tisch reservieren")
    print("[L]: Reservierung löschen")
    print("[F]: Freie Tische ausgeben")
    print("[T]: Tischliste ausgeben")
    print("[E]: Exit")

    wahl = input()
    wahl_upper = wahl.upper()

    if wahl_upper == "R":
        tischReservieren()
    elif wahl_upper == "L":
        reservierungLoeschen()
    elif wahl_upper == "F":
        printFreieTische()
    elif wahl_upper == "T":
        printTischListe()
    elif wahl_upper == "E":
        exit()
    else:
        print("Fehlerhafte Eingabe. Programm wird beendet.")
        exit()
