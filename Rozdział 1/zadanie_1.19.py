# Wyświetl wszystkie liczby podzielne przez 6 ze zbioru od 0 do 1000 włącznie. [1]
for i in range(0, 1001):
    if 0 == i % 6:
        print(str(i))
