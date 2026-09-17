#Odgadnij wzór ciągu, a następnie wyświetl jego sto elementów. Początek ciągu:
#100,99,97,94,90,85,.... [2]
start :int = 100
odejmowana :int = 1
for i in range(0, 100):
    print(str(start))
    start -= odejmowana
    odejmowana += 1