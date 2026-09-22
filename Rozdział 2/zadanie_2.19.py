#Dla losowego całkowitego n z zakresu <5;12> narysuj „trójkąt prostokątny”.
#Przykładowo, dla n=5 ma to wyglądać tak:
#
##
###
####
#####
#W ostatnim wierszu ma być pięć (ogólnie n) znaków '#', a w pierwszym — jeden
#znak '#'. Następnie narysuj podobny trójkąt, ale tak, by najdłuższy bok nie był
#z lewej, ale z prawej strony. [2]
    #
   ##
  ###
 ####
#####
import random
los : int = random.randint(5,12)
for i in range(0 ,los):
    liczba_znakuw :int = i
    for j in range(0, los):
        if liczba_znakuw >= j:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
liczba_znakuw: int = 0
for i in range(0, los):
    for j in range(0, los):
        if j >= los -liczba_znakuw :
            print("#", end="")
        else:
            print(" ", end="")
    print("")
    liczba_znakuw += 1