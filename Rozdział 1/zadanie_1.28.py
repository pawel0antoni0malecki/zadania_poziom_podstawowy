# Pobieraj w pętli jeden znak (char). Ignoruj znaki niebędące znakami cyfr. Przerwij
# pętlę, gdy zbierzesz pięć znaków będących cyframi, np. '1', '4', '3', '5', '0'.
# Utwórz zmienną całkowitą, która będzie liczbą utworzoną z tych cyfr. Ma to być
# faktyczna zmienna, np. typu long long int. Dla podanego przykładu byłaby to
# liczba 14 350. [2]
wektor: list[str] = []
liczba: int = 0
while len(wektor) < 5:
    znak: str = input("podaj cyfre : ")
    if znak.isnumeric():
        wektor.append(znak)
while len(wektor) != 0:
    liczba *= 10
    liczba += int(wektor[0])
    wektor.pop(0)
print(str(liczba))
