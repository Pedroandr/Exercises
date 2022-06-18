word = input('Digite a palavra:\n> ')
lett = input ('Digite a letra:\n> ')

def count(letra, pala):
    index = 0
    for letter in pala:
        if letter == letra:
            index = index+1
    print(f'a letra se repete {index} vezes')

count(lett, word)
