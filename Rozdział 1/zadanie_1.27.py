# Utwórz trzy wektory z następującą zawartością: v1={1,3,5,7,9}, v2={1,4,7,11,15},
# v3={1,2,3,4,5,6,7,8,9,20} (plik 27_vectory.txt) Potraktuj je jak zbiory, w któ-
# rych każdy element może wystąpić tylko jeden raz. Przykładowo, po dodaniu
# do zbioru v1 liczby 5, zbiór nie uległby zmianie, gdyż 5 już tam jest. Dla podanych
# wektorów/zbiorów wyświetl:
# a) część wspólną zbiorów: v1 i v2, [1,]
# b) różnicę zbioru v3 i sumy zbiorów v1+v2: v3–(v1+v2), [4,]
# c) sumę wszystkich zbiorów v1, v2 i v3: v1+v2+v3. [2]
V1: list[int] = [1, 3, 5, 7, 9]
V2: list[int] = [1, 4, 7, 11, 15]
V3: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
print(set(V1) | set(V2))
print(set(V3) - (set(V1) | set(V2)))
print(set(V1) | set(V2) | set(V3))
