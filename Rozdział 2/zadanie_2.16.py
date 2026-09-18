#Pobierz lub wylosuj liczbę całkowitą n z zakresu <5;12>. Następnie dla tego n
#narysuj „kwadrat” złożony ze znaków #, który ma n wierszy i n kolumn (czyli n
#znaków w wierszu). Na przykład dla n=5:
#####
#####
#####
#####
#####
#Zrób z tego funkcję rysującą dla podanej liczby i znaku. [1]
import random
ilosc :int = random.randint(5,12)
for i in range(0, ilosc):
    for j in range(0, ilosc):
        print("#", end=" ")
    print("")