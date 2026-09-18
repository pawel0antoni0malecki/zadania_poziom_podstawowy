#Utwórz tablicę/wektor dwudziestu losowych liczb typu double z zakresu od –1 do 1
#i precyzją do trzech miejsc po przecinku. Oblicz średnią wszystkich liczb. [2]
import random
wektor :list[float] = []
srednia :float = 0
for i in range(0, 20):
    liczba :float= round(random.random(), 3)
    if 1 == random.randint(0,1):
        liczba *= -1
    srednia += liczba
    wektor.append(liczba)
srednia /= 20
print(srednia)
print(wektor)