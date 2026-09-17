# W podanym ciągu poszukaj wszystkich podciągów, których suma wynosi 10. Pokaż
# elementy je tworzące i pozycje tych elementów (ciąg znajduje się również w pliku
# 38_ciag.txt). Przez podciąg rozumiemy fragment zbioru składający się z sąsia-
# dujących ze sobą liczb, czyli np. podciąg czteroelementowy to dowolne cztery
# sąsiadujące ze sobą liczby z początkowego zbioru/wektora, jedna po drugiej,
# bez omijania jakiejkolwiek. Na przykład {1,2,3,2} to podciąg składający się
# z pierwszych czterech liczb całego ciągu. [3]
# {1,2,3,2,5,6,9,1,3,7,5,8,0,9,3,1,2,5,7,6,3,4,2,1,0,8,9,7,8,4,6,3,2,5,4,7,8,9,1,3,2,5,
# 4,7,5,6,8,0,1,2,3,6,5,8,7,1,1,2,3,4,4,5,5,6,8,9,0,9,8,1,9,7,5,4,1,2,7,6,9,3,4,2,6};
wektor: list[int] = [
    1,
    2,
    3,
    2,
    5,
    6,
    9,
    1,
    3,
    7,
    5,
    8,
    0,
    9,
    3,
    1,
    2,
    5,
    7,
    6,
    3,
    4,
    2,
    1,
    0,
    8,
    9,
    7,
    8,
    4,
    6,
    3,
    2,
    5,
    4,
    7,
    8,
    9,
    1,
    3,
    2,
    5,
    4,
    7,
    5,
    6,
    8,
    0,
    1,
    2,
    3,
    6,
    5,
    8,
    7,
    1,
    1,
    2,
    3,
    4,
    4,
    5,
    5,
    6,
    8,
    9,
    0,
    9,
    8,
    1,
    9,
    7,
    5,
    4,
    1,
    2,
    7,
    6,
    9,
    3,
    4,
    2,
    6,
]
wektory: list[list[int]] = []
for i in range(0, len(wektor)):
    suma: int = 0
    pod_ciong: list[int] = []
    for j in range(i, len(wektor)):
        suma += wektor[j]
        pod_ciong.append(wektor[j])
        if suma == 10:
            i = j
            wektory.append(pod_ciong)
            break
        elif suma > 10:
            break
print(wektory)
