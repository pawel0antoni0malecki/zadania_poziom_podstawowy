#Utwórz wektor zawierający następujące cyfry (można skopiować z pliku
#26_vector.txt):
#vector<int> v={1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9};
#Znajdź w wektorze i wyświetl wszystkie podciągi trójelementowe (trzy kolejne
#liczby wektora), które tworzą ciągi niemalejące. [1,]
#Znajdź jeden najdłuższy podciąg niemalejący. [3,]
#Policz liczbę wystąpień każdej liczby w wektorze. [2]
zbiur :list[int] = [1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9]
pod_zbiur :list[int] = []
zbiory :list[list[int]] = []
for i in range(0, 22):
    if zbiur[i] <= zbiur[i+1] and zbiur[i+1] <= zbiur[i+2]:
        print(str(zbiur[i])+" "+str(zbiur[i+1])+" "+str(zbiur[i+2]))

for i in range(0, len(zbiur)-1):
    if zbiur[i] <= zbiur[i+1]:
        pod_zbiur.append(zbiur[i])
    elif zbiur[i] >= zbiur[i-1]:
        pod_zbiur.append(zbiur[i])
        print(pod_zbiur)
        zbiory.append(pod_zbiur)
        pod_zbiur = []
if len(pod_zbiur) >= 1 and (pod_zbiur[len(pod_zbiur)-1] <= zbiur[len(zbiur)-1]):
        pod_zbiur.append(zbiur[len(zbiur)-1])
        zbiory.append(pod_zbiur)
        pod_zbiur = []
elif len(pod_zbiur) >= 1:
    zbiory.append(pod_zbiur)
    pod_zbiur = []
print(zbiory)
numer_zbioru :int = 0
najktutszy : int = 0
for i in range(0, len(zbiory)-1):
    if len(zbiory[i]) > najktutszy:
        numer_zbioru = i
        najktutszy = len(zbiory[i])
print(zbiory[numer_zbioru])