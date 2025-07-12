
print("Hello feladatmegoldó")

# Gyakorló feladatok
# 1. Feladat Egy függvényt tesztelünk amely két szám szorzatát adja vissza eredményül.

def ketszam_szorzat():
    print("Egy függvényt tesztelünk, amely két szám szorzatát adja vissza eredményül")

    elsoszam = int(input("első szám: "))
    masodikszam = int(input("második szám: "))

    print(elsoszam * masodikszam)

ketszam_szorzat()

#2. Feladat Egy függvényt tesztelünk, amely két szám közül adja vissza a kisebb dupláját

def kisebb_dupla():
    print("Adj meg kétszámot és a kisebbet kétszer megszorzom")

    elso = int(input("első szám: "))
    masodik = int(input("második szám: "))

    if elso > masodik:
        print(masodik * 2)
    else:
        print(elso * 2)

kisebb_dupla()

#3 Feladat Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan-e.

def paros_paratlan():

    print("Adj meg egy számot és kitalálom hogy páros vagy páratlan.")

    parosparatlan = int(input("A szám: "))

    if parosparatlan % 2 == 0:
        print("páros")
    else:
        print("páratlan")

paros_paratlan()

#4 Feladat Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb háromszorosát.

def nagyobbtripla():
    print("Adj meg kétszámot és a nagyobbat háromszor megszorzom")

    elso3 = int(input("első szám: "))
    masodik3 = int(input("második szám: "))

    if elso3 < masodik3:
        print(masodik3 * 3)
    else:
        print(elso3 * 3)

nagyobbtripla()