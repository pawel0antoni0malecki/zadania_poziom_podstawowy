#Pobierz pięć liczb z klawiatury i wyświetl informację, ile spośród nich było pa-
#rzystych, a ile nieparzystych. [1]
parzyste: int = 0
nie_parzyste: int = 0
for i in range(0, 5):
     if 0 == int(input("Podaj liczbę nr " + str(i+1) + " : ")) % 2:
        parzyste += 1
     else:
        nie_parzyste += 1
print("Liczb parzystych jest : "+str(parzyste))
print("Liczby nie_parzystych jest : "+str(nie_parzyste))