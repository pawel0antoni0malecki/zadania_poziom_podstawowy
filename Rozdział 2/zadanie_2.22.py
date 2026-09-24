#Dla naturalnego N >= 3 narysuj „choinkę” złożoną z piramid („trójkątów”):
  #
 ###
##### (pierwsza, szczytowa piramidka)
#Każda kolejna część choinki ma mieć piramidkę o jeden wiersz dłuższą, a łączna

#liczba piramid tworzących choinkę ma być równa N. Pierwsza piramidka two-
#rząca czubek choinki ma być zawsze złożona z trzech linii. Przykład dla N=3:

    #
   ###
  #####
    #
   ###
  #####
 #######
    #
   ###
  #####
 #######
######### (N=3 -> trzy piramidki tworzące choinkę)
#Oczywiście choinka ma być symetryczna, czyli środkowa kolumna każdej piramidy
#ma być w tej samej kolumnie co środkowe kolumny pozostałych piramid. [4]
import random
rand_int :int = random.randint(3, 5)
max_width = 2 * (rand_int + 2) - 1

for i in range(1, rand_int + 1):          # k-ta piramidka (1, 2, 3, ...)
    rows = i + 2                   # liczba wierszy tej piramidki (3, 4, 5, ...)
    for j in range(1, rows + 1):
        width = 2 * j - 1          # liczba znaków '#' w tym wierszu
        spaces = (max_width - width) // 2
        print(' ' * spaces + '#' * width)
