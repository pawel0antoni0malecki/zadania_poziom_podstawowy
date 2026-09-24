# Pobierz pięć liczb z klawiatury. Jeżeli tworzą ciąg rosnący (zgodnie z kolejnością
# pobierania), poinformuj o tym. [1]
zbiur: list[int] = []
zbiur.append(int(input("Podaj liczbę nr 1 : ")))
zbiur.append(int(input("Podaj liczbę nr 2 : ")))
zbiur.append(int(input("Podaj liczbę nr 3 : ")))
zbiur.append(int(input("Podaj liczbę nr 4 : ")))
zbiur.append(int(input("Podaj liczbę nr 5 : ")))
test: bool = True
for i in range(0, 4):
    if zbiur[i] > zbiur[i + 1]:
        test = False
if test:
    print("zbiur jest rosnący")
else:
    print("zbiur nie jest rosnący")
