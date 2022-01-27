fuehrerschein = input("Bitte geben Sie die Führerscheinnummer ein: ")

value = 0
multiplicator = 9
for char in fuehrerschein[0:9]:
    if char.isalpha():
        value += int((ord(char)-55) * multiplicator)
    else:
        value += (int(char) * multiplicator)
    multiplicator -= 1

checksum = fuehrerschein[9]
calculated_checksum = value % 11
if calculated_checksum == 10 and checksum == 'X' or calculated_checksum == int(checksum):
    print("Führerschein gültig")
else:
    print("Führerschein ungültig")