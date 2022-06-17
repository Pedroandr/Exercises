
'''a função -avoids- apenas verifica se a palavra existe ou não'''
def avoids(word, letter):
    if letter in word:
        print ('A palavra contem a letra digitada')
    else:
        print ('A palavra não contem a letra digitada')

'''Essa função -inputs- recebe os valores e passa para o verificador -avoids-'''
def inputs():
    word_inp = input('Digite a palavra:_ ')
    letters = input('Digite a letra:_ ')

    avoids(word_inp, letters)


inputs()