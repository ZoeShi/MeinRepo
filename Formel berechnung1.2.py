import math

def KreisUmfang(r):
    print(2 * math.pi * r)

def FlächeninhaltKreis(r):
    print(math.pi * r ** 2)

def VolumenKugel(r):
    print(4 / 3 * math.pi * r ** 3)

def QuadratVolumen(a):
    print(a ** 3)
    
def FlächeninhaltQuadrat(a):
    print(a ** 2)

def FlächeninhaltQuader(a, b):
    print(a * b)

def FlächeninhaltParallelogram(a, h):
    print(a * h)

def FlächeninhaltRaute(e, f):
    print(e * f / 2)

def FlächeninhaltTrapez(a, c, h):
    print(a + c / 2 * h)
    
def FlächeninhaltDreieck(c, h):
    print(1 / 2 * c * h)
    
def FlächeninhaltRechtwinkligesDreieck(a, b):
    print(a * b / 2)

def VolumenPyramide(a, b, h):
    print(1 / 3 * a * b * h)

def VolumenZylinder(r, h):
    print(math.pi * r ** 2 * h)

loopCondition = True

while loopCondition:

    eingabe = input("Bitte geben sie eine Formel ein: ")

    if eingabe == "hilfe":
        print("diese Formel Berechnungen gibt es")
        print("KreisUmfang")
        print("FlächeninhaltKreis")
        print("VolumenKreis")
        print("QuadratVolumen")
        print("FlächeninhaltQuadrat")
        print("FlächeninhaltQuader")
        print("FlächeninhaltParallelogram")
        print("FlächeninhaltRaute")
        print("FlächeninhaltTrapez")
        print("FlächeninhaltDreieck")
        print("FlächeninhaltRechtwinkligesDreieck")
        print("VolumenPyramide")
        print("VolumenZylinder")
        print("zum beenden quit eingeben")
        print("Die Groß und Kleinschreibung muss beachtet werden!")
    elif eingabe == "KreisUmfang":
        r = float(input("Bitte geben sie einen Radius ein: "))
        KreisUmfang(r)
    elif eingabe == "FlächeninhaltKreis":
        r = float(input("Bitte geben sie einen Radius ein: "))
        FlächeninhaltKreis(r)
    elif eingabe == "VolumenKugel":
        r = float(input("Bitte geben sie einen Radius ein: "))
        VolumenKreis(r)
    elif eingabe == "QuadratVolumen":
        a = float(input("Bitte geben sie seite a ein: "))
        QuadratVolumen(a)
    elif eingabe == "FlächeninhaltQuadrat":
        a = float(input("Bitte geben sie seite a ein: "))
        FlächeninhaltQuadrat(a)
    elif eingabe == "FlächeninhaltQuader":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        FlächeninhaltQuader(a, b)
    elif eingabe == "FlächeninhaltParallelogram":
        a = float(input("Bitte geben sie seite a ein: "))
        h = float(input("Bitte geben sie höhe zu a ein: "))
        FlächeninhaltParallelogram(a, h)
    elif eingabe == "FlächeninhaltRaute":
        e = float(input("Bitte geben sie e ein: "))
        f = float(input("Bitte geben sie f ein: "))
        FlächeninhaltRaute(e, f)
    elif eingabe == "FlächeninhaltTrapez":
        a = float(input("Bitte geben sie die länge a ein: "))
        c = float(input("Bitte geben sie die länge c ein: "))
        h = float(input("Bitte geben sie die höhe zu a ein: "))
        FlächeninhaltTrapez(a, c, h)
    elif eingabe == "FlächeninhaltDreieck":
        c = float(input("Bitte geben sie seite c ein: "))
        h = float(input("Bitte geben sie höhe zu c ein: "))
        FlächeninhaltDreieck(c, h)
    elif eingabe == "FlächeninhaltRechtwinkligesDreieck":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        FlächeninhaltRechtwinkligesDreieck(a, b)
    elif eingabe == "VolumenPyramide":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        h = float(input("Bitte geben sie höhe ein: "))
        VolumenPyramide(a, b, h)
    elif eingabe == "VolumenZylinder":
        r = float(input("Bitte geben ein radius ein: "))
        h = float(input("Bitte geben höhe ein: "))
        VolumenZylinder(r, h)
    elif eingabe == "quit":
        loopCondition = False

        
