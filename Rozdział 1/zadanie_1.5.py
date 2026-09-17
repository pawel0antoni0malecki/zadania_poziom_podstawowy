# Masz takie wyrażenie: (((a1+a2)*a3)-a4)/a5 (elementy od a1 do a5 są typu float).
# Pobierz z klawiatury każdą ze zmiennych a1 do a5, oblicz wartość wyrażenia
# i wyświetl wynik. [1]
numer: list[float] = []
for i in range(0, 5):
    numer.append(float(input("podaj liczbę numer " + str(i + 1) + ": ")))
print("wynik : " + str((((numer[0] + numer[1]) * numer[2]) - numer[3]) / numer[4]))
