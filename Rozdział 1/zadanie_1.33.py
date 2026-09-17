#Skopiuj poniższy wektor do swojego kodu lub skopiuj go z pliku 33_wektor.txt.
#vector<int> x = { 2,7,1,1,4,9,3,2,1,4,1,9,6,1,3,0,1,2,3,6,8,5,6,9,
#3,0,8,1,8,8,7,0,7,8,5,0,2,2,3,7,1,7,2,4,7,7,5,9,0,7,7,9,2,2,2,7,
#0,0,5,4,6,3,9,3,5,1,0,0,9,2,9,2,8,5,0,8,5,7,0,9,6,4,9,7,8,8,6,5,
#4,3,2,5,8,9,4,6,8,7,9,9 };
#Odpowiedz na następujące pytania:
#a) Ile razy wystąpiła sytuacja, w której dwie sąsiednie liczby były
#identyczne? [1,]
#b) Ile razy wystąpiła sytuacja, w której dwie sąsiednie liczby łącznie
#miały wartość 10? [1]
wektor :list[int] = [2,7,1,1,4,9,3,2,1,4,1,9,6,1,3,0,1,2,3,6,8,5,6,9,
3,0,8,1,8,8,7,0,7,8,5,0,2,2,3,7,1,7,2,4,7,7,5,9,0,7,7,9,2,2,2,7,
0,0,5,4,6,3,9,3,5,1,0,0,9,2,9,2,8,5,0,8,5,7,0,9,6,4,9,7,8,8,6,5,
4,3,2,5,8,9,4,6,8,7,9,9]
powturki :int = 0
dziesiontki :int = 0
for i in range(0 ,len(wektor)-1):
    if wektor[i] == wektor[i+1]:
        powturki += 1
    if wektor[i] + wektor[i+1] == 10:
        dziesiontki += 1
print("powturek było : " + str(powturki))
print("suma 2 liczb daje 10 : " + str(dziesiontki))