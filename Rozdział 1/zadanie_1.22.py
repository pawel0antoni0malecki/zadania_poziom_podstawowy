# Pobieraj liczby z klawiatury i wkładaj je do tablicy/wektora. Pobieranie ma się
# zakończyć, gdy zostanie wprowadzona dwa razy z rzędu taka sama liczba. [1]
zbiur: list[int] = []
zbiur.append(int(input("podaj liczbę : ")))
while True:
    zbiur.append(int(input("podaj liczbę : ")))
    if zbiur[len(zbiur) - 2] == zbiur[len(zbiur) - 1]:
        break
