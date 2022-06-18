fin = open(r'Exercícios\Ex9\words.txt')

'''a função -avoids- apenas verifica se a palavra existe ou não e printá-la'''
def avoids(word, letter):
    if letter not in word:
        print(word)

'''Essa função -inputs- recebe os valores e passa para o verificador -avoids-'''
def inputs():
    letters = input('Digite a letra:_ ')
    
    for line in fin:
        avoids (line, letters)

inputs()