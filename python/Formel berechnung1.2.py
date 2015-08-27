import math

def kreisumfang(r):
    print(2 * math.pi * r)

def flaecheninhaltkreis(r):
    print(math.pi * r ** 2)

def volumenkugel(r):
    print(4 / 3 * math.pi * r ** 3)

def quadratvolumen(a):
    print(a ** 3)
    
def flaecheninhaltquadrat(a):
    print(a ** 2)

def flaecheninhaltquader(a, b):
    print(a * b)

def flaecheninhaltparallelogram(a, h):
    print(a * h)

def flaecheninhaltraute(e, f):
    print(e * f / 2)

def flaecheninhalttrapez(a, c, h):
    print(a + c / 2 * h)
    
def flaecheninhaltdreieck(c, h):
    print(1 / 2 * c * h)
    
def flaecheninhaltrechtwinkligesdreieck(a, b):
    print(a * b / 2)

def volumenpyramide(a, b, h):
    print(1 / 3 * a * b * h)

def volumenzylinder(r, h):
    print(math.pi * r ** 2 * h)

loopCondition = True

while loopCondition:

    eingabe = input("Bitte geben sie eine Formel ein: ")

    if eingabe == "hilfe":
        print("diese Formel Berechnungen gibt es")
        print("KreisUmfang")
        print("FlaecheninhaltKreis")
        print("VolumenKreis")
        print("QuadratVolumen")
        print("FlaecheninhaltQuadrat")
        print("FlaecheninhaltQuader")
        print("FlaecheninhaltParallelogram")
        print("FlaecheninhaltRaute")
        print("FlaecheninhaltTrapez")
        print("FlaecheninhaltDreieck")
        print("FlaecheninhaltRechtwinkligesDreieck")
        print("VolumenPyramide")
        print("VolumenZylinder")
        print("zum beenden quit eingeben")
        print("Die Groß und Kleinschreibung muss beachtet werden!")
    elif eingabe == "KreisUmfang":
        r = float(input("Bitte geben sie einen Radius ein: "))
        kreisumfang(r)
    elif eingabe == "FlaecheninhaltKreis":
        r = float(input("Bitte geben sie einen Radius ein: "))
        flächeninhaltkreis(r)
    elif eingabe == "VolumenKugel":
        r = float(input("Bitte geben sie einen Radius ein: "))
        volumenkreis(r)
    elif eingabe == "QuadratVolumen":
        a = float(input("Bitte geben sie seite a ein: "))
        quadratvolumen(a)
    elif eingabe == "FlaecheninhaltQuadrat":
        a = float(input("Bitte geben sie seite a ein: "))
        flächeninhaltquadrat(a)
    elif eingabe == "FlaecheninhaltQuader":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        flächeninhaltquader(a, b)
    elif eingabe == "FlaecheninhaltParallelogram":
        a = float(input("Bitte geben sie seite a ein: "))
        h = float(input("Bitte geben sie höhe zu a ein: "))
        flächeninhaltparallelogram(a, h)
    elif eingabe == "FlaecheninhaltRaute":
        e = float(input("Bitte geben sie e ein: "))
        f = float(input("Bitte geben sie f ein: "))
        flächeninhaltraute(e, f)
    elif eingabe == "FlaecheninhaltTrapez":
        a = float(input("Bitte geben sie die länge a ein: "))
        c = float(input("Bitte geben sie die länge c ein: "))
        h = float(input("Bitte geben sie die höhe zu a ein: "))
        flächeninhalttrapez(a, c, h)
    elif eingabe == "FlaecheninhaltDreieck":
        c = float(input("Bitte geben sie seite c ein: "))
        h = float(input("Bitte geben sie höhe zu c ein: "))
        flächeninhaltdreieck(c, h)
    elif eingabe == "FlaecheninhaltRechtwinkligesDreieck":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        flächeninhaltrechtwinkligesdreieck(a, b)
    elif eingabe == "VolumenPyramide":
        a = float(input("Bitte geben sie seite a ein: "))
        b = float(input("Bitte geben sie seite b ein: "))
        h = float(input("Bitte geben sie höhe ein: "))
        volumenpyramide(a, b, h)
    elif eingabe == "VolumenZylinder":
        r = float(input("Bitte geben ein radius ein: "))
        h = float(input("Bitte geben höhe ein: "))
        volumenzylinder(r, h)
    elif eingabe == "quit":
        loopCondition = False

        
