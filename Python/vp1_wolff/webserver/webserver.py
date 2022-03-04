import random, time

while True:

    gewicht_donald = random.randint(1, 8)
    gewicht_benjamin = random.randint(1000, 2000)
    gewicht_simba = random.randint(80, 250)
    gewicht_gesamt = gewicht_simba + gewicht_benjamin + gewicht_donald
    gewicht_mittel = gewicht_gesamt/3
    with open("index.html", "w") as datei:
        datei.write("""<html>
        <head>
            <meta http-equiv="refresh" content="1"> 
            <title>Testtitel</title>
        </head>
        <body>
        <h1>Sebastian stinkt nach Fisch</h1>
        Benjamin, der kleine Elefant, wiegt: """ + str(gewicht_benjamin) + """ kg.<br>
        Simba, der mutige Löwe, wiegt: """ + str(gewicht_simba) + """ kg.<br>
        Donald, die dumme Ente, wiegt: """ + str(gewicht_donald) + """ kg.<br>
        </body>
        </html>
    """)
    time.sleep(1)
