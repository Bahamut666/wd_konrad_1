print('hello world')

def main():
    pass

# łańcuchy znaków
imie = "Marian"
print(imie)
print(type(imie))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))
print(imie[2])
#imie[0] = "D" #str nie jest mutowalny
imie = "Darian"
imie = imie.lower()
print(imie)
wiek = 30
#print(imie + "ma" + wiek + "lat") nie zadziała
print(imie + "ma" + wiek.__str__() + "lat.")
print(imie + "ma" + str(wiek) + "lat.")
print("{} ma {} lat.".format(imie, wiek))
print("{0} ma {1} lat.".format(imie, wiek))
#f-string
print(f"{imie} ma {wiek} lat.")
# pyformat.info
liczba = 6.75647464736363
print(f"{liczba:>.2f}")

#typ liczbowy
liczba = 5
liczbaf = 5.5
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2) #dzielenie bez reszty
print(1 ** 2) #potęgowanie
print(1 % 2) # modulo
tekst = "110"
liczba_z_tekstu = int(tekst, 2)
print(liczba_z_tekstu)
import math
pi = 3.15
from math import *
from math import pow, sqrt, pi
import math as m
#m.pow()
print(m.pi)

#listy
lista = [] #pusta lista
lista2 = list() #pusta lista
lista3 = [1, 2, 3]
lista3 = [1, "Ala", True, None, [1, 2]]
lista3[1] = "Zosia"
#lista3[1][0] = "O"
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(macierz[1][1])
print(0.1 + 0.2 == 0.3)
#Decimal
print(f"{0.1:.5f}")
lista = lista + lista3
lista += lista3

#słowniki
slownik = {}
slownik = dict()
slownik3 = {"klucz": "wartosc"}
slownik3['klucz'] = 100
slownik3[0] = 999
print(slownik3)