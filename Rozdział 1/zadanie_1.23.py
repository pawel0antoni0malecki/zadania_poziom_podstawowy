#Pobieraj liczby z klawiatury i wkładaj je do wektora pod warunkiem, że taka
#liczba jeszcze w wektorze nie istnieje. Jeżeli istnieje, zignoruj ją i pobieraj dalej.
#Pobieranie zakończy się, gdy wektor będzie zawierał dziesięć liczb. [2]
zbiur :list[int] = []
while(len(zbiur) < 10):
    dostana = int(input("podaj liczbę : "))
    if dostana not in zbiur:
        zbiur.append(dostana)
print(zbiur)