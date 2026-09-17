# Sprawdź, czy trzy zmienne typu float mogą utworzyć trójkąt prostokątny, przy
# założeniu, że wartości zmiennych są długościami boków. Dla ułatwienia przyjmij,
# że zmienne są zawsze >0. Jeżeli istnieje możliwość utworzenia trójkąta, poin-
# formuj o tym odpowiednią wiadomością. Możesz wykorzystać to, że w trójkącie
# prostokątnym suma kwadratów długości przyprostokątnych wynosi tyle samo,
# ile kwadrat długości przeciwprostokątnej: (a^2+b^2=c^2). [1]
wektor: list[int] = []
for i in range(0, 3):
    wektor.append(int(input("podaj liczbę numer " + str(i + 1) + " : ")))
if (
    ((wektor[0] * wektor[0]) + (wektor[1] * wektor[1]) == (wektor[2] * wektor[2]))
    or ((wektor[2] * wektor[2]) + (wektor[1] * wektor[1]) == (wektor[0] * wektor[0]))
    or ((wektor[2] * wektor[2]) + (wektor[0] * wektor[0]) == (wektor[1] * wektor[1]))
):
    print("to jest trujkąt prostokątny")
else:
    print("to nie jest trujkąt prostokątny")
