#Narysuj „kwadrat” złożony ze znaków '#' dla dowolnego całkowitego n z prze-
#działu <5;12>. Jedno z wewnętrznych pól (wylosuj które) ma być znakiem '@',

#a nie znakiem '#'. Nie może to być krawędź „kwadratu”! [1,] Na przykład:
#####
##@##
#####
#####
#####
#Następnie zrób to samo, ale kwadrat ma być pusty w środku (spacje) i posiadać
#tylko krawędzie. Znak '@' ponownie nie może znajdować się na krawędzi. [2]
#####
# @ #
#   #
#   #
#####
import random
rand_int :int = random.randint(5,12)
hight :int = random.randint(1,rand_int-2)
large :int = random.randint(1,rand_int-2)
for i in range(0, rand_int):
    for j in range(0 ,rand_int):
        if hight == i and large == j:
            print("@", end="")
        else:
            print("#", end="")
    print("")
print("")
for i in range(0, rand_int):
    for j in range(0 ,rand_int):
        if hight == i and large == j:
            print("@", end="")
        elif i == 0 or i == rand_int - 1 or j == 0 or j == rand_int - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("")