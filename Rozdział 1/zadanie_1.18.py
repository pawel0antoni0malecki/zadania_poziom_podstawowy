#Pobieraj liczbę z klawiatury i wyświetlaj jej dwukrotność. Operację powtarzaj,
#dopóki nie zostanie wpisana wartość pomiędzy 1 a 10 włącznie. [1]
while(True):
    liczba :int = int(input("Podaj mi liczbę : "))
    liczba *= 2
    print(str(liczba))
    if liczba <= 10 and liczba >= 1:
        break