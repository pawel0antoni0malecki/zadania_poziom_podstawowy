#Pobraną z klawiatury liczbę całkowitą zweryfikuj pod kątem parzystości.
#Wyświetl tak lub nie, gdy jest lub nie jest parzysta. [1]
numer = int( input("podaj liczbę : "))
if 0 == numer % 2:
    print("Ta liczba jest parzysta.")
else:
    print("Ta liczba jest nie parzysta.")