# Odgadnij wzór ciągu, a następnie wyświetl jego sto elementów. Początek ciągu:
# 1,2,2,3,3,3,4,4,4,4,.... [2]'=
startowa: int = 1
powturki: int = 0
for i in range(1, 101):
    print(startowa)
    powturki += 1
    if startowa == powturki:
        startowa += 1
        powturki = 0
