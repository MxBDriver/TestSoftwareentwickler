# Variablendeklaration
summe = 0.0     # Summe der eingegebenen Zahlen
anzahl = 0      # Anzahl der eingegebenen Zahlen

# Fortlaufende Eingabe von Gleitpunkt-Zahlen
while True:
    eingabe = input("Gib eine Zahl ein (oder 'x' zum Beenden): ")

    # Überprüfen, ob die Eingabe 'x' ist
    if eingabe.lower() == 'x':
        break

    # Eingabe in eine Gleitkommazahl umwandeln
    zahl = float(eingabe)

    # Berechnung des neuen Mittelwerts
    summe = (summe * anzahl) + zahl
    anzahl += 1
    mittelwert = summe / anzahl

    # Ausgabe des neuen Mittelwerts
    print("Der aktuelle Mittelwert beträgt:", mittelwert)

# Ende des Programms
print("Programm beendet.")
