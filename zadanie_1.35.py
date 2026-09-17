#Wstaw do wektora v dziesięć dowolnych liczb całkowitych. Korzystając tylko
#z iteratora zwracanego przez funkcję v.begin()/v.end() lub korzystając z funkcji
#v.front()/v.back(), wyświetl wszystkie jego elementy (w dowolnej kolejności,
#żadnego nie pomijając). [1]
#Możesz przestawiać elementy wektora i je usuwać. Nie możesz jednak w żadnym
#momencie użyć notacji z pozycją, np. v[0], ani wykorzystać pętli jak w przykła-
#dzie poniżej:
#for (auto e : v)
wektor :list[int] = []
for i in range(0 ,10):
    znak :str = input("podaj znak : ")
    if znak.isalpha():
        wektor.append(ord(znak))
    elif znak.isnumeric():
        wektor.append(int(znak))
print(wektor)