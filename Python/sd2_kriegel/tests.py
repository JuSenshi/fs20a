import random as r  # für Mischen

liste = [42, 69, 10, -2, -5, 0, 8, 17, 24, -7]

##### Berechnungen / Ermitltungen #####
# Maximum ermitteln
print(max(liste))
# Minimum ermitteln
print(min(liste))
# Summe
print(sum(liste))
# Durchschnitt
print(sum(liste) / len(liste))

##### FORMATIERUNGEN #####
# Sortieren
liste.sort()
print(liste)
# Mischen
r.shuffle(liste)
print(liste)

##### FILTER #####
# Ausgabe aller negativen Werte
for val in liste:
    if val < 0:
        print(val)

# Ausgabe aller geraden Werte
for val in liste:
    if val % 2 == 0:
        print(val)
