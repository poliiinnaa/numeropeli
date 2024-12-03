import random

# Tietokone arpoo numeron väliltä 1-100
oikea_numero = random.randint(1, 100)

print("Tervetuloa Numeron Arvaus -peliin!")
print("Tietokone on arvonnut numeron väliltä 1-100.")

while True:
    arvaus = int(input("Anna arvauksesi: "))

    if arvaus < oikea_numero:
        print("Liian pieni!")
    elif arvaus > oikea_numero:
        print("Liian suuri!")
    else:
        print("Oikein! Numero oli:", oikea_numero)
        break
