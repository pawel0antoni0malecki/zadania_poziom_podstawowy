#Wyświetl liczby całkowite od 1 do 120 włącznie, z pominięciem liczb podzielnych
#równocześnie przez 11 i 5. Wyświetl informacje, ile liczb się wyświetliło, a ile
#zostało pominiętych. [1]
wypisano :int = 0
pominiento :int = 0
for i in range(1, 121):
    if not (0 == i % 5 and 0 == i % 11):
        print(i)
        wypisano += 1
    else:
        pominiento += 1
print("wypisano : " + str(wypisano))
print("pominiento : " + str(pominiento))