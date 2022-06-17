def verT():
    Aside = input('Digite o lado A do triângulo.\n')
    Bside = input('Digite o lado B do triângulo.\n')
    Cside = input('Digite o lado C do triângulo.\n')

    if Aside>(Bside+Cside):
        print('No')

    elif Bside>(Aside+Cside):
        print('No')

    elif Cside>(Aside+Cside):
        print('No')

    else:
        print('Yes')
        
verT()