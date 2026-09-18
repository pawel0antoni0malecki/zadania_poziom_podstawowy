#Wypełnij wektor losowymi liczbami całkowitymi, następnie wszystkie liczby
#parzyste wyzeruj, a nieparzystym zmień znak, po czym wyświetl ten wektor od
#tyłu (od elementu ostatniego do pierwszego). Ilość liczb w wektorze ma być
#również losowa: od 10 do 100 włącznie, a same liczby — dowolne. [1]
import random
ilosc :int = random.randint(1, 1000)
wektor :list[int] = []
for i in range(0 ,ilosc):
    wektor.append(random.randint(10,100))
for i in range(0,len(wektor)):
    if 0 == wektor[i] % 2:
        wektor[i] = 0
    else:
        wektor[i] *= -1
print(wektor)
