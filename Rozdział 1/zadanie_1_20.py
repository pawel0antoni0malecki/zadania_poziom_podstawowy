# Utwórz wektor i wstaw do niego dziesięć dowolnych liczb. Utwórz drugi wektor,
# który na początku zawiera liczby parzyste z pierwszego wektora, a potem po-
# zostałe. Wyświetl oba wektory. [1]
import random

wektor: list[int] = []
wektor_2: list[int] = []

for i in range(0, 10):
    wektor.append(random.randint(1, 100))

for i in range(0, len(wektor)):
    if 0 == wektor[i] % 2:
        wektor_2.append(wektor[i])

for i in range(0, len(wektor)):
    if 0 != wektor[i] % 2:
        wektor_2.append(wektor[i])
print(wektor)
print(wektor_2)
