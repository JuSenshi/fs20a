iban = input("Bitte geben Sie ihre IBAN ein: ")

value = 0
counter = 0
first_four = ""
iban_as_list = list(iban.replace(" ", ""))
iban_as_list[2] =0
iban_as_list[3] =0
iban = ''.join(str(c) for c in iban_as_list)
for i in range(4):
    first_four += str(iban_as_list[i])
    iban = iban[:0] + iban[0+1:]
iban += first_four

print("first_four", first_four)
print("iban", iban)

for char in iban:
    if char.isalpha():
        print(char)
        iban.replace(char, str((ord(char)-55)))


print(iban)
#
# checksum = fuehrerschein[9]
# calculated_checksum = value % 11
# if calculated_checksum == 10 and fuehrerschein[9] == 'X' or calculated_checksum == int(checksum):
#     print("Führerschein gültig")
# else:
#     print("UNGÜLTIG")
#
# print(fuehrerschein[9])
# print(checksum)
# print(value)
