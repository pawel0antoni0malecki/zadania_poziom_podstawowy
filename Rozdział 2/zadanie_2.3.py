#Losuj w pętli dowolną angielską literę małą lub dużą tak długo, aż zostanie wylo-
#sowana mała litera 'z' lub duża 'A'. Podaj liczbę losowań po zakończeniu działa-
#nia pętli. Wylosowane litery umieszczaj w napisie. Pokaż tak uzyskany napis. [1]

import random
wektor :list[str] = []
while(True):
    if 1 == random.randint(0,1):
        znak_asci :int = random.randint(65,90)
    else:
        znak_asci :int = random.randint(97,122)

    znak :str = chr(znak_asci)
    wektor.append(znak)
    if znak == "z" or znak == "A":
        break

print(wektor)

