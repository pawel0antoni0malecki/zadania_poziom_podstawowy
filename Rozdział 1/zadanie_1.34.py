# Pobieraj w pętli znak (char) z klawiatury. Za każdym razem po pobraniu znaku wy-
# świetlaj jego wartość całkowitą (int). Gdy suma tych wartości uzyskana z kolej-
# nych znaków przekroczy 350, zakończ pętlę. Wyświetlaj również po pobraniu
# znaku aktualny stan sumy. [1,]
# Ogranicz się do małych i dużych liter angielskich oraz cyfr. Jeżeli zostanie wpro-
# wadzony inny znak, zignoruj go. [1]
suma: int = 0
while suma <= 350:
    znak: str = input("podaj znak : ")
    if znak.isnumeric():
        suma += int(znak)
        print("podano znak : " + str(int(znak)))
        print("suma znakuw : " + str(suma))
    elif znak.isalpha():
        suma += ord(znak)
        print("podano znak : " + str(ord(znak)))
        print("suma znakuw :" + str(suma))
