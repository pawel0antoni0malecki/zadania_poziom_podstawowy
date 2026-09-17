# Dla dwóch liczb, int A i int B, wykonaj operację mnożenia (A*B), nie korzy-
# stając ze znaku mnożenia *. Wykonaj to samo dla A typu float oraz B typu int,
# ale tym razem nie możesz użyć * ani / (mnożenia ani dzielenia). [1]
liczba_1: int = int(input("podaj liczbę nr 1 : "))
liczba_2: int = int(input("podaj liczbę nr 2 : "))
wynik: int = 0
for i in range(0, liczba_1):
    wynik += liczba_2
print(str(liczba_1) + " * " + str(liczba_2) + " = " + str(wynik))
