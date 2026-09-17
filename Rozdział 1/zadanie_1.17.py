#Odgadnij wzór ciągu, a następnie wyświetl jego sto elementów. Początek ciągu:
#6,2,8,3,10,4,12,5,14,6,.... [1]
start_1 :int = 6
start_2 :int = 2
for i in range(0, 50):
    print(str(start_1)+" "+str(start_2))
    start_1 += 2
    start_2 += 1