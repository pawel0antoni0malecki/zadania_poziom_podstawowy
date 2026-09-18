#Wykorzystuj operator bitowy &, aby sprawdzać, czy liczba nieujemna jest parzysta.
#Utwórz funkcję sprawdzającą w ten sposób parzystość i zwracającą true/false
#(parzysta/nieparzysta). [1]
import random
def test(liczba:int) -> bool:
    if liczba & 2 != 0:
        return True
    else:
        return False

liczba :int = random.randint(0,100000)
test_wynik :bool = test(liczba)
print("czy liczba "+str(liczba)+" jest parzysta : "+str(test_wynik))