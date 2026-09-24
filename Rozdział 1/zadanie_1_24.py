# Pobieraj z klawiatury znaki (bez polskich ogonków i bez dużych liter) i wprowa-
# dzaj je do wektora według zasady: samogłoski zawsze na początku wektora, po-
# zostałe znaki na końcu wektora. Jeżeli pojawi się znak * lub #, nie wstawiaj ich,
# tylko usuń z wektora pierwszy znak (dla *) lub ostatni (dla #), o ile jest co usuwać.
# Zakończ pętlę pobierania i wstawiania, gdy wprowadzony będzie znak !. [2]
znak: str = "z"
zbiur: list[str] = []
while znak != "!":
    znak = input("podaj znak : ")
    if znak == "*" and len(zbiur) >= 1:
        zbiur.pop(0)
    elif znak == "#" and len(zbiur) >= 1:
        zbiur.pop()
    else:
        zbiur.append(znak)

print(zbiur)
