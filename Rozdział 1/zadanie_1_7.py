# Pobieraj znaki z klawiatury aż do wprowadzenia znaku x. Ile znaków pobrano? [1]
ile_podano: int = 0
while True:
    if "x" == input("podaj znak : "):
        ile_podano += 1
        break
    else:
        ile_podano += 1
print("podano " + str(ile_podano) + " znaków")
