#Utwórz pętlę, która losuje liczbę z zakresu od 1 do 1000 włącznie, ale po każ-
#dym kroku zmienia zakres losowania od ostatnio wylosowanej liczby do 1000
#włącznie. Pętla przerywa się, gdy wylosujesz 1000. Przykładowo, pierwsze lo-
#sowanie jest z zakresu <1;1000> i np. wypada 200. Zatem drugie losowanie jest
#z zakresu <200;1000> i np. wypada 254. Zatem trzecie losowanie ma być doko-
#nane z zakresu <254;1000> itd. Wylosowane liczby mają być zwracane w wek-
#torze przez funkcję. [2]
import random
def los(wektor:list[int]) -> None:
    wektor.append(random.randint(wektor[len(wektor)-1], 1000))
wektor :list[int] = [1]
while(wektor[len(wektor)-1] < 1000):
    los(wektor)
print(wektor)