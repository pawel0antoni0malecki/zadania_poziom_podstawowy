#Pobierz liczbę całkowitą z klawiatury i wykonaj na niej poniższe operacje: jeżeli
#liczba była ujemna, zmniejsz ją o 1; jeżeli liczba była dodatnia, zwiększ ją o 1;
#jeżeli była zerem, pozostaw bez zmian; Wyświetl liczbę po zmianach. Następnie
#określ parzystość liczby po zmianach i wyświetl informację na ten temat
#(tak/nie). [1]
numer :int = int(input("podaj liczbe : "))
if numer > 0:
    numer += 1
elif numer < 0:
    numer -= 1
print("liczba po zmianach : "+str(numer))
print("czy liczba jest parzysta : "+ str(0 == numer % 2))