#Pobierz z klawiatury dwie liczby całkowite a, b. Utwórz funkcję zwracającą liczbę
#double, gdzie a to część całkowita, a wartość bezwzględna z b to część ułamkowa
#zwracanej liczby. Na przykład dla 45 i –11 zwróć 45.11. [2]
import random
liczba_1 :int = int(input("Podaj liczbę nr 1 : "))
liczba_2 :int = int(input("Podaj liczbę nr 2 : "))
def loncze(liczba_1:int, liczba_2:int) -> float:
    liczba :float = liczba_1
    liczba += (abs(liczba_2))/10**(len(str(liczba_2))-1)
    return liczba
liczba :float = loncze(liczba_1,liczba_2)
print("liczba połączona "+str(liczba))