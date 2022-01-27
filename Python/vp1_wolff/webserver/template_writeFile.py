import time

with open("index.html", "w") as datei:
    datei.write("""
    <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beschreibung der Seite (erscheint in der Titelzeile des Browsers)</title>
  </head>
  <body>
    <p>Dieser Text wird im Browserfenster angezeigt.</p>
  </body>
</html>
    """)
time.sleep(2)
