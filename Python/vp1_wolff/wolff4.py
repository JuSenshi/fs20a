import math
# TODO: Attribute im Konstruktor zu int konvertieren lassen (macht Zeile 44 unnötig)


class Bruch:
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner

    def addierenNeu(self, bruch):
        zaehler = self.zaehler * bruch.nenner + self.nenner * bruch.zaehler
        nenner = self.nenner * bruch.nenner
        return Bruch(zaehler, nenner)

    def multiplizierenNeu(self, bruch):
        zaehler = self.zaehler * bruch.zaehler
        nenner = self.nenner * bruch.nenner
        return Bruch(zaehler, nenner)
    # Alternative 1:
        # return Bruch(self.zaehler * bruch.zaehler, self.nenner * bruch.nenner)

    def addieren(self, bruch):
        self.zaehler = self.zaehler * bruch.nenner + self.nenner * bruch.zaehler
        self.nenner = self.nenner * bruch.nenner

    def print(self):
        print(self.zaehler, "/", self.nenner, sep="")

    def kuerzen(self):
        gcd = math.gcd(self.zaehler, self.nenner)
        self.zaehler = self.zaehler // gcd
        self.nenner = self.nenner // gcd


# Inputs
abfragen = True
listeAllerBrueche = []

while abfragen:
    eingabeBruch = input("Geben Sie den Bruch nach folgendem Format ein: Zähler/Nenner: ")
    bruchGetrennt = eingabeBruch.split("/")

    # Umwandeln des Zählers und Nenners in Integers
    bruchGetrennt = list(map(int, bruchGetrennt))
    # Hinzufügen des Bruches zur Liste
    listeAllerBrueche.append(Bruch(bruchGetrennt[0], bruchGetrennt[1]))

    testinput = input("Möchten Sie einen weiteren Bruch eingeben? (y/N): ")
    if testinput != "y":
        abfragen = False


x = listeAllerBrueche[0].addierenNeu(listeAllerBrueche[1])
x.print()
x.kuerzen()
x.print()

# Alternative zu addierenNeu
listeAllerBrueche[0].addieren(listeAllerBrueche[1])
listeAllerBrueche[0].kuerzen()
listeAllerBrueche[0].print()
