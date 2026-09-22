#Wylosuj nieparzyste całkowite n z zakresu <7;21> (jeśli będzie parzyste, losuj
#ponownie), a następnie narysuj „piramidę”, w której w pierwszym wierszu jest
#jeden znak '#', a w drugim są trzy znaki '#' itd. W ostatnim wierszu ma być n
#znaków.
#Następnie narysuj „diament”, czyli początkowo to samo, ale po osiągnięciu naj-
#dłuższej (ostatniej) linii znaków '#' rysuj odbicie lustrzane, traktując tę ostat-
#nią linię jak oś symetrii. Efektem ma być figura jak w przykładzie niżej dla n=7:

   #
  ###
 #####
####### (najdłuższa linia (symetria pozioma) dla n=7 znaków)
 #####
  ###
   #
#Zadbaj o to, aby obie figury rysowała funkcja otrzymująca jako argumenty znak n. [3]
import random
rand_int :int = 0
while(0 == rand_int % 2):
    rand_int = random.randint(7,21)
line :int = 0
half :int = rand_int // 2
for i in range(0 ,rand_int):
    for j in range(0 ,rand_int):
        if j + line >= half and j <= line + half:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
    if i < half:
        line += 1
    else:
        line -= 1
print(rand_int)

