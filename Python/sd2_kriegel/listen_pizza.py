# -----------------------------------------------------------
# Übungsaufgabe zum EVA-Prinzip und der Nutzung von Listen anhand des Beispiels
# einer Sammlung von Lieblingspizzen
# Styleguide: https://google.github.io/styleguide/pyguide.html
# -----------------------------------------------------------
def print_list(given_list):
    index = 1
    for slots in given_list:
        print(index, ":", slots)
        index += 1


pizzen = input("Bitte geben Sie Ihre Lieblingspizzen ein. Bitte durch Kommata trennen: ")
pizza_varianten = pizzen.split(",")

# Bereinigen von leeren Inputs (List-Call notwendig, da sonst ein iterator von filter zurückgegeben wird)
pizza_varianten = list(filter(None, pizza_varianten))
# Alternative:
# for variante in pizza_varianten:
#     if variante == "":
#         pizza_varianten.remove("")

menu = "test"
while menu != "":
    menu = input("\nMöchten Sie\n"
                 "(E) weitere Pizzen ergänzen?\n"
                 "(S) die Liste sortieren?\n"
                 "(L) einen Eintrag löschen?\n"
                 "Bestätigen Sie nur mit Enter, um Ihre Liste auszugeben: ").upper()

    if menu == "E":
        ergaenzung = input("Geben Sie bitte den Namen der zu ergänzenden Pizza ein: ")
        # Mehrzeiler
        if ergaenzung != "" and not ergaenzung.isnumeric():
            pizza_varianten.append(ergaenzung)
        else:
            print("Fehlerhafte Eingabe.")
        # Methode 2 - Ternärer Operator
        # pizza_varianten.append(ergaenzung) if ergaenzung != "" and not ergaenzung.isnumeric() else print("Fehler!")

    elif menu == "S":
        # TODO: Auswahl, ob aufsteigend oder absteigend
        pizza_varianten.sort()
        print("Die Liste wurde alphabetisch sortiert.")

    elif menu == "L":
        print_list(pizza_varianten)
        loeschen = input("Welche Pizza soll gelöscht werden, geben Sie die Nummer oder den Namen ein: ")

        try:
            # Methode 1 - Ternärer Operator
            pizza_varianten.pop(int(loeschen) - 1) if loeschen.isnumeric() else pizza_varianten.remove(loeschen)
            # Methode 2 - Zweizeiler if/else:
            # if loeschen.isnumeric(): pizza_varianten.pop(int(loeschen) - 1)
            # else: pizza_varianten.remove(loeschen)
            # Methode 3 - Vierzeiler if/else:
            # if loeschen.isnumeric():
            #     pizza_varianten.pop(int(loeschen)-1)
            # else:
            #     pizza_varianten.remove(loeschen)
            print("Ihre Pizza wurde erfolgreich gelöscht.")
        except (IndexError, ValueError):  # Hier kann man theoretisch die Exceptions einzeln ansprechen
            print("Die Eingabe war fehlerhaft. Es konnte nichts gelöscht werden.")

    elif menu == "":
        print("Eingabe leer. Ihre Liste wird nun ausgegeben:")
        print_list(pizza_varianten)
    else:
        print("Fehlerhafte Eingabe. Bitte versuchen Sie es erneut.")
