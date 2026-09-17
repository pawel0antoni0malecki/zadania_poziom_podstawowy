# Wyświetl swoje imię w pętli tyle razy, ile jest w tym imieniu samogłosek (uwzględ-
# nij sześć samogłosek, to jest "eyuioa"). [1]

imie: str = input("Podaj imie ")
wektor: list[str] = ["e", "y", "u", "i", "o", "a"]
wypisz: int = 0
for i in imie:
    if i in wektor:
        wypisz += 1
for i in range(0, wypisz):
    print(imie)
