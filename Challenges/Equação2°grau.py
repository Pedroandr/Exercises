#----------Exercício de equação de segundo grau--------------
Aelement = int(input('Digite o elemento A da equação: '))
Belement = int(input('Digite o elemento B da equação: '))
Celement = int(input('Digite o elemento C da equação: '))
#________________________________________________________
#----------------------Fórmulas--------------------------
delta = (Belement**2 -4 * Aelement * Celement)
Xlinha = ((-Belement) + delta ** 0.5 / 2 * Aelement)
X2linhas = ((-Belement) - delta ** 0.5 / 2 * Aelement)
print('O delta é: ',delta)
print('O X1 é: ',Xlinha)
print('O X2 é: ',X2linhas)