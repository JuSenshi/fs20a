def zwei_eins():
    print("Willkommen")


def zwei_zwei(counter):
    for i in range(counter):
        print("Willkommen")


def zwei_drei(counter):
    for i in range(counter):
        print("Willkommen")
    return len("Willkommen") * counter


def drei_eins(netto):
    return float(netto) * 1.19


def drei_zwei(name):
    return name[:3]


def kasten(name, zeichen, anzahl):
    print(zeichen * anzahl)
    print(name)
    print(zeichen * anzahl)


def kasten2(name, zeichen="*", anzahl=5):
    kasten(name, zeichen, anzahl)


print("2.1:")
zwei_eins()
print("2.2:")
zwei_zwei(10)
print("2.3:")
test = zwei_drei(2)
print(zwei_drei(2))
print("3.1:")
print(drei_eins(1))
print("3.2:")
print(drei_zwei("Krieger"))
print("AB 5; 1A:")
kasten("Krieger", "*", 10)
kasten2("test", "-", 5)
kasten2(name="Krieger", anzahl=18)
