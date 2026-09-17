# Pobierz znak (char) z klawiatury. Sprawdź, czy to samogłoska, spółgłoska, czy
# cyfra. Poinformuj o tym, jaki to znak. Uwzględnij tylko małe litery alfabetu an-
# gielskiego i cyfry. [1]
numery: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
samogloski: list[str] = ["a", "e", "i", "o", "u", "y"]
spulglosk: list[str] = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "r",
    "s",
    "t",
    "w",
    "z",
]
znak = input("Podaj znak albo liczbę. : ")
if znak in numery:
    print("To jest liczba " + znak)
elif znak in samogloski:
    print("To jest samogłoska " + znak)
elif znak in spulglosk:
    print("To jest spółgłoska " + znak)
else:
    print("Nie wiem co to.")
