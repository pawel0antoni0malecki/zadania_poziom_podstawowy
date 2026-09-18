#Wygeneruj dwadzieścia losowych liczb całkowitych od 0 do 20. Za każdym razem,
#gdy wylosujesz taką liczbę, umieszczaj ją w wektorze na losowej pozycji. Nie
#możesz jednak nadpisać istniejących już w wektorze wartości. Pokaż zawartość
#wektora, gdy osiągnie wielkość dwudziestu liczb. [2]
import random
wektor :list[int] = []
for i in range(0 ,20):
    wektor.insert(random.randint(0, len(wektor)), random.randint(0 ,20))
print(wektor)
