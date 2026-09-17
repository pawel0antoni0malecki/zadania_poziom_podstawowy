# Skopiuj do wektora następujące znaki:
# {'x','P','Q','4','\n','%','u','@','e',
#'T','B','$', '!',':','"','1','<','d','k','L','$',')','$','B','x',
#'w','q','P','c','X','B','>','?','[','r','x','$', '#','}','|','d',
#'l','n','b','V','!'};
# (znajdują się one również w pliku 39_znaki.txt). Wyświetl te znaki z wektora,
# które się powtórzyły, ale nie leżą na jego początku ani końcu. Wyświetl je jeden
# raz. Podaj sumę, którą tworzą wszystkie występujące w wektorze znaki będące
# cyfrą (np. znak '8' i znak '2' daje sumę 10).
wektor: list[str] = [
    "x",
    "P",
    "Q",
    "4",
    "\n",
    "%",
    "u",
    "@",
    "e",
    "T",
    "B",
    "$",
    "!",
    ":",
    '"',
    "1",
    "<",
    "d",
    "k",
    "L",
    "$",
    ")",
    "$",
    "B",
    "x",
    "w",
    "q",
    "P",
    "c",
    "X",
    "B",
    ">",
    "?",
    "[",
    "r",
    "x",
    "$",
    "#",
    "}",
    "|",
    "d",
    "l",
    "n",
    "b",
    "V",
    "!",
]
powturki: list[str] = []
suma: int = 0
for i in range(0, len(wektor)):
    for j in range(i + 1, len(wektor)):
        if wektor[i] == wektor[j]:
            if wektor[i] not in powturki:
                print("znak się powtarza : " + wektor[i])
                powturki.append(wektor[i])
    if wektor[i].isnumeric():
        suma += int(wektor[i])
print("suma liczb w zbiorze : " + str(suma))
