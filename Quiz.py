
import random

while True:
    eingabe1 = input("Was ist der Befehl für Ordner erstellen? ")
    if eingabe1 == 'mkdir':
        print("richtig")
    else:
        print("Das ist leider falsch")
        print("Die richtige Antwort lautet mkdir")
    eingabe2 = input("Was ist der Befehl für Ordner wechseln? ")
    if eingabe2 == 'cd':
        print("richtig")
    else:
        print("Das ist leider falsch")
        print("Die richtige Antwort lautet cd")
    eingabe3 = input("Was ist der Befehl für Verzeichnis anzeigen lassen? ")
    if eingabe3 == 'pwd':
        print("richtig")
    else:
        print("Das ist leider falsch")
        print("Die richtige Antwort lautet pwd")
    eingabe4 = input("Was ist der Befehl für herunterfahren ? ")
    if eingabe4 == 'shutdown':
        print("richtig")
    else:
        print("Das ist leider falsch")
        print("Die richtige Antwort lautet shutdown")
    eingabe5 = input("Was ist der Befehl für neustarten? ")
    if eingabe5 == 'reboot':
        print("richtig")
        break
    else:
        print("Das ist leider falsch")
        print("Die richtige Antwort lautet reboot")
        break
