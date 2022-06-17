from imaplib import Int2AP


def hypotenuse(cat1, cat2):
    som = cat1**2 + cat2**2
    hyp = som**.5
    print(hyp)

CatA = int(input('>Digite o valor de um cateto:\n'))
CatB = int(input('>Digite o valor do outro cateto:\n'))

hypotenuse(CatA, CatB)