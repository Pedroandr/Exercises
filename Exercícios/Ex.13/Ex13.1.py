livv = open('Exercícios\Ex.13\pg67724.txt', encoding="utf8")

word_per_line = []
count_words = {}

#this function works for the list
def takesecound(di):
    return di[1]

#this function sorts the itens of the dictionary
def srtd(d):
    nd = list(zip(d.keys(), d.values()))
    nd.sort(key=takesecound)
    count = 1
    nd.reverse()
    while count != 21:
        print (f'{count}-{nd[count]}')
        count += 1

#this function attaches the numbers of the word repetitions
def trat():
    global word_per_line
    global count_words
    for word in word_per_line:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    srtd(count_words)

#this function splits every word of the book in itens of the "word_per_line" list
def splitwords():
    global word_per_line

    for line in livv:
        l = line.lower()
        word_per_line = word_per_line + l.split()
    trat()

splitwords()