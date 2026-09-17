#Wylosuj trzy liczby i umieść je w wektorze. Utwórz funkcję, która znajduje naj-
#większą liczbę w przekazanym do niej wektorze i zwraca ją, a z wektora usuwa.
#Jeżeli liczba ta wystąpiła w wektorze wiele razy, usuń tylko jedną, dowolną.
#Wyświetl sumę pozostałych liczb tyle razy, ile wynosiła ta maksymalna liczba.
#Na przykład dla 1,2,3. wyświetlasz trzy razy sumę 1+2. [2]
import random

def maxint(wektor:list[int]) -> int:
    max_int :int = 0
    pozycja = 0
    for i in range(0,len(wektor)):
        if wektor[i] > max_int:
            max_int = wektor[i]
            pozycja = i
    wektor.pop(pozycja)
    return max_int

wektor :list[int] = []
for i in range(0, 3):
    wektor.append(random.randint(0,100))
print(wektor)
print(maxint(wektor))
print(wektor)



