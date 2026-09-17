# Pobierz z klawiatury dwie liczby (float) i znak działania (jeden z tych: *, +, –, /).
# W zależności od znaku wykonaj na pobranych dwóch liczbach odpowiednie
# działanie i poinformuj o wyniku. Zwróć uwagę na dzielenie przez 0! Przykład:
# dla pobranej liczby 3 i 9.5 oraz znaku + zwróć sumę 12.5. [2]
numer_1: float = float(input("liczba nr 1 : "))
numer_2: float = float(input("liczby nr 2 : "))
znak: str = input("podaj znak : ")
if znak == "+":
    print(
        str(numer_1) + " " + znak + " " + str(numer_2) + " = " + str(numer_1 + numer_2)
    )
elif znak == "-":
    print(
        str(numer_1) + " " + znak + " " + str(numer_2) + " = " + str(numer_1 - numer_2)
    )
elif znak == "*":
    if numer_1 != 0 and numer_2 != 0:
        print(
            str(numer_1)
            + " "
            + znak
            + " "
            + str(numer_2)
            + " = "
            + str(numer_1 * numer_2)
        )
    else:
        print(str(numer_1) + " " + znak + " " + str(numer_2) + " = 0")
elif znak == "/":
    if numer_1 != 0 and numer_2 != 0:
        print(
            str(numer_1)
            + " "
            + znak
            + " "
            + str(numer_2)
            + " = "
            + str(numer_1 / numer_2)
        )
    else:
        print(str(numer_1) + " " + znak + " " + str(numer_2) + " = 0")
