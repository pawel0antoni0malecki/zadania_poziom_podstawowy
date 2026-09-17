#Pobieraj w pętli liczby z klawiatury. Wkładaj je do wektora V. Wnętrze pętli to
#następujące kroki:
#1. Pobierz liczbę i wprowadź ją na koniec wektora.
#2. Pobierz liczbę i wprowadź ją na koniec wektora (tak, takie same
#polecenie w ramach kroku pętli).
#3. Jeżeli iloczyn dwóch ostatnich liczb z wektora nie przekracza 1000,
#wprowadź również ten iloczyn do wektora V i wróć do punktu 1., a jeżeli
#ten iloczyn przekroczył wartość 1000, zakończ pętlę. [1]
znak :int
V :list[int] = []
while(True):
    znak = int(input("podaj znak : "))
    V.append(znak)
    V.append(znak)
    V.append(V[len(V)-1] * V[len(V)-2])
    if V[len(V)-1] > 1000:
        break
print(V)