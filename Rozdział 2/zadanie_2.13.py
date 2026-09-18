#Pobierz znak z klawiatury, a następnie wylosuj dwie liczby całkowite a, b w za-
#kresie od 5 do 10 każda. Utwórz funkcję, która otrzyma te wartości jako argu-
#menty i narysuje a wierszy, w których będzie b znaków (znak pobrany z klawia-
#tury na początku). Na przykład dla znaku # i liczb 3 i 8 narysuj trzy wiersze
#w każdym po osiem znaków #. [2]
import random
znak :str = input("podaj znak : ")
liczby_1 :int = random.randint(5,10)
liczby_2 :int = random.randint(5,10)
def draw(liczby_1:int, liczby_2:int, znak:str) -> None:
    for i in range(0,liczby_1):
        for j in range(0, liczby_2):
            print(znak,end=" ")
        print("")
draw(liczby_1, liczby_2, znak)
print(liczby_1)
print(liczby_2)