def verT():
    Aside = input('Digite o lado A do triângulo.\n')
    Bside = input('Digite o lado B do triângulo.\n')
    Cside = input('Digite o lado C do triângulo.\n')

    if Aside>(Bside+Cside):
        print('As três retas não formam um triângulo.')

    elif Bside>(Aside+Cside):
        print('As três retas não formam um triângulo.')

    elif Cside>(Aside+Cside):
        print('As três retas não formam um triângulo.')

    else:
        print('As três retas formam um triângulo.')
        
verT()
