import random as rdm
import time

name = "localhost"

while True:
    f=open("index.html", "w")

    temp1 = rdm.randrange(15, 25)
    temp2 = rdm.randrange(15, 25)
    temp3 = rdm.randrange(15, 25)


    htmlcode="""
    <html>
    <head>
        <meta charset="UTF-8">
        <title> Temperatur </title>
        <style>
            body{
                background-color: #424242;
                color: white;
            }
            #rainbow{
                background: -webkit-linear-gradient(left, orange , yellow, green, cyan, blue, violet);
                background: linear-gradient(to right, orange , yellow, green, cyan, blue, violet);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 10vw;
            }
        </style>
    </head>
    <body>
        <h1>Temperaturmessung</h1>
        <p>Auf dieser Webseite werden Temperaturen angezeigt.<br>
        Ist das nicht cool?</p>
        <ul>
            <li>"""+str(temp1)+"""
            <li>"""+str(temp2)+"""
            <li>"""+str(temp3)+"""
        </ul>
        <p id="rainbow"> Over the rainbow</p>
        <img src="cloudy.png">
    </body>
    </html>"""

    f.write(htmlcode)
    f.close()
    time.sleep(0.1)