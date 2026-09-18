#Wylosuj liczbę całkowitą L między 20 a 30 włącznie oraz pobierz z klawiatury
#znak Z. Wyświetl L-krotnie znak Z. [1]
import  random
l :int = random.randint(20,30)
znak :str = input("podaj znak ")
for i in range(0,l):
    print(str(i)+" : "+str(znak))