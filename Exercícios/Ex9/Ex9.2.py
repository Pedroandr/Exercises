fin = open('Exercícios\Ex9\words.txt')


def find():
    lines = 0
    without_e = 0

    #varredura
    for word in fin:
        lines = lines+1
        if word.find('e') == True:
            without_e = without_e+1
    
    #placar e cálculos
    print(f'{without_e} palavras contêm a letra E num total de {lines}.')

    def calc(li, ca):
        a = ca*100
        b = a/li
        if b < 1:
            print(f'a porcentagem é {b}%')
        else:
            print(f'a porcentagem é {int(b)}%')
    
    calc(lines, without_e)

find()

