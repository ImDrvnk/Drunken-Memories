#program następujący :
# wczytać z konsoli liczbe (najpierw)
# a następnie wczytać teskt
# a potem wypisać liczbe i tekst (najpierw tekst)

# zczytywanie z konsoli -> input()
# wypisywanie do konsoli -> print(arg)
import time
print ("Podaj liczbe:")
liczba = input()

while int(liczba) > 999:
    print("Zbyt duża liczba")
    liczba = input()

print("Podaj tekst:")
tekst = input()

while tekst.__len__() < 4:
    print ("Co zrobiłeś z zaoszczędzonym czasem?")
    tekst = input()

print (liczba+ " " + "i" + " " + tekst)
time.sleep(3)
print ("Działa :D")
