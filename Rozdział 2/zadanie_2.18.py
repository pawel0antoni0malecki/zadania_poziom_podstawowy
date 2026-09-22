#Dla losowego całkowitego n z zakresu <5;12> narysuj „kwadrat” składający się
#z n wierszy i n kolumn, którego krawędź to znak '#', a wnętrze jest puste (spacje).
#Na przykład: [1]
#####
#   #
#   #
#   #
#####
import random
rand_int = random.randint(5, 12)
for i in range(0,rand_int):
    for j in range(0 ,rand_int):
        if i == 0 or i == rand_int - 1:
            print("#", end="")
        elif j == 0 or j == rand_int -1:
            print("#", end="")
        else:
            print(" " ,end="")
    print("")