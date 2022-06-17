def avoids(word, letter):
    Wrd_avoid = word
    Carac_avoid = letter
    if Wrd_avoid in Carac_avoid:
        print ('A palavra contem a letra digitada')
    else:
        print ('A palavra não contem a letra digitada')
    
def inputs():
    word_inp = input('Digite a palavra:_ ')
    letters = input('Digite a letra:_ ')

    avoids(word_inp, letters)


inputs()