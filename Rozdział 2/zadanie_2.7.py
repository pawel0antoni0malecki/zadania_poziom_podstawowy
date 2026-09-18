#Wylosuj dwadzieścia liczb z zakresu od 0 do 1000 każda i wyświetl trzy najwięk-
#sze z nich. [2]
import random
wektor :list[int] = []
for i in range(0, 20):
    wektor.append(random.randint(0, 1000))
wektor.sort()
print(wektor)
print("liczby największe "+str(wektor[len(wektor)-1])+" "+str(wektor[len(wektor)-2])+" "+ str(wektor[len(wektor)-3]))