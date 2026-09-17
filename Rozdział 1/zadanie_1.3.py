#Pobierz liczbę całkowitą z klawiatury i sprawdź, czy jest podzielna: przez 3
#i przez 5; przez 3, ale nie przez 5; przez 5, ale nie przez 3; ani przez 3, ani przez 5.
#Właściwą odpowiedź wyświetl na ekranie. [1]
numer = int(input("Podaj liczbę : "))
if 0 == numer % 3 and 0 == numer % 5:
    print(str(numer) + " Jest podzielna przez 3 i przez 5.")
elif 0 == numer % 3 and 0 != numer % 5:
    print(str(numer) + " Jest podzielna przez 3 i nie jest przez 5.")
elif 0 != numer % 3 and 0 == numer % 5:
    print(str(numer) + " Nie jest podzielna przez 3 ale jest podzielna przez 5.")
elif 0 != numer % 3 and 0 != numer % 5:
    print(str(numer) + " Nie jest podzielna przez 3 i nie jest przez 5.")
else:
    print("To nie liczba!")