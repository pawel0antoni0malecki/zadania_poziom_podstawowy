#Pewien kosmiczny blob, okrążający swoją gwiazdę, postanowił zwiększyć swoją
#masę. Na początku blob ważył 1 kg i przez pierwsze dwa okrążenia swojej gwiazdy
#nie udało mu się wzrosnąć. Ale przy trzecim okrążeniu blob ważył tyle, ile wy-
#nosiła suma wartości jego wagi z ostatnich dwóch okrążeń. Od tego momentu
#wszystko potoczyło się błyskawicznie. Kolejne okrążenie ponownie zaowoco-
#wało wagą bloba równą sumie wag z ostatnich dwóch okrążeń i ten schemat
#trwał już cały czas. Ile wynosiła waga kosmicznego bloba po trzynastym okrąże-
#niu macierzystej gwiazdy? Przyjmij, że dwa pierwsze okrążenia to waga 1 i 1. [3]
wektor :list[int] = [1,1]
for i in range(1, 12):
    wektor.append(wektor[i]+wektor[i-1])
print(wektor)
print("waga po 13 orbitach : "+str(wektor[len(wektor)-1]))