fin = open('Exercícios\Ex9\words.txt')
lines = 0
carac = 0

for line in fin:
    lines = lines+1
    if len(line) >= 20:
        carac = carac+1
        word = line.strip()
        print(word)

print(f'{carac} palavras contêm vinte ou mais caracteres de um total de {lines} palavras')

def calc(li, ca):
    a = ca*100
    b = a/li
    print(f'a porcentagem é {b}%')

calc(lines, carac)

