#Wyświetlaj losowe liczby całkowite od 0 do 100 tak długo, aż wypadnie 100.
#Wyświetl informację, ile losowań nastąpiło, zanim przerwała się pętla przy
#wartości 100. [1]
import random
wektor :list[int] = []
ilosc :int = 0
while(True):
    wektor.append(random.randint(0,100))
    ilosc += 1
    if wektor[len(wektor)-1] == 100:
        break
print("liczb losowanych było : "+str(ilosc))