#Pobierz z klawiatury trzy nieujemne liczby całkowite. Znajdź największą z nich.
#Wyświetl sumę pozostałych liczb tyle razy, ile wynosi wartość największej
#liczby.
numer : list[int] = []
for i in range(1, 4):
    numer.append( int( input("podaj liczbe numer " + str(i) + " ")))
if numer[0] >= numer[1] and numer[0] >= numer[2]:
    numer.append(numer[1] + numer[2])
    for i in range(0, numer[0]):
        print( str(numer[3]) + "   ")
elif numer[1] >= numer[0] and numer[1] >= numer[2]:
    numer.append(numer[0] + numer[2])
    for i in range(0, numer[1]):
        print( str(numer[3]) + "   ")
else:
    numer.append(numer[0] + numer[1])
    for i in range(0, numer[2]):
        print( str(numer[3]) + "   ")
