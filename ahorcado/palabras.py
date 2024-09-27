# Extrae las palabras de words.txt
# Y genera una Lista con ellas

from random import randint

def ran_word():

    file = open('words.txt', 'r')

    words = file.readlines()

    file.close()

    num_words = len(words)
    
    word = words[randint(0, num_words)]

    return word

if __name__ == '__main__':
    ran_word()

