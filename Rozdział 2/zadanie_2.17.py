#Dla losowego całkowitego n z zakresu <5;12> narysuj szachownicę ze znaku '#'
#oraz spacji ' '. [2] Na przykład dla n=5:
# # #
 # #
# # #
 # #
# # #
import random
liczba :int = random.randint(5,12)

for i in range(0 ,liczba):
    parzystosc :int = i % 2
    for j in range(0, liczba):
        if j == liczba - 1 and 1 == i % 2:
            break
        elif parzystosc == 0:
            print("#", end="")
            parzystosc = 1
        else:
            print(" ", end="")
            parzystosc = 0
    print("")
print(liczba)