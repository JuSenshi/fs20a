#MiBs = Mbps*10**6 / 8 / 2**20



#FE6F -> 1111 1110 0110 1111
#Bitflip +1 -> 0000 0001 1001 0001
#Binär aus Tabelle ->

print(2**4 + 2**3 + 2**0 + 2**-4)


Hexzahl = int(input("Hexzahl: "), 16)

if Hexzahl > 2047:
    Hexzahl = ((Hexzahl ^ 0xFFFF) +1)*(-1)

print ("Temperatur: ", Hexzahl/16, "°C")


#setMode(GPIO.BCM)
#setup(pin, GPIO.out)