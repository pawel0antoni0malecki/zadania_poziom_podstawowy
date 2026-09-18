#Wypełnij dziesięcioelementową tablicę/wektor losowymi liczbami całkowitymi
#z zakresu od –10 do 10. Ile jest liczb ujemnych w tak wylosowanej tablicy, ile
#jest liczb dodatnich, ile parzystych, a ile nieparzystych? [1]
import  random
wektor :list[int] = []
dodatnia :int = 0
parzystych :int = 0
for i in range(0, 10):
    wektor.append(random.randint(-10,10))
    if wektor[i] >= 0:
        dodatnia += 1
    if 0 == wektor[i] % 2:
        parzystych += 1
print(wektor)
print("liczb dodatnich jest : " + str(dodatnia) + ". liczb ujemnych jest : "+ str(10 -dodatnia))
print("liczb parzystych jest : " + str(parzystych) + ". liczb nie parzystych jest : "+ str(10 -parzystych))