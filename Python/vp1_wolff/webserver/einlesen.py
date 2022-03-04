import requests, re
html = requests.get("http://localhost:8000")

print(html.text)

gewicht_gesamt = 0
counter = 0
pattern = r"\d+ kg"
for number in re.finditer(pattern, html.text):
    gewicht_instanz = number.group().replace(" kg", "")
    gewicht_gesamt += gewicht_instanz
    counter += 1

print("Gesamtgewicht:", gewicht_gesamt, "kg | Mittelwert:", gewicht_gesamt/counter, "kg")


