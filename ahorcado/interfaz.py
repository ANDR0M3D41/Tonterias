images = [
    '''    
    |   |
        |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
        |
        |
        |
        =''',
    '''
    
    |   |
    O   |
    |   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|   |
        |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
        |
        |
        =''',
    '''
   
    |   |
    O   |
   /|\  |
    |   |
        |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =''',
    '''
    
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ='''
]

def user_word_create(lenght):

    list_word = []

    for i in range(0, lenght):
        
            list_word.append('_')

    return list_word

        
def game(word):

    len_word = len(word) - 1
        
    firt_for = 1

    lifes = len(images)

    char_user = ''

    user_word = user_word_create(len_word)

    while lifes > 0:
       
        iterations = 0 # For Loop

        correct = 0

        print(images[-abs(lifes)])

        print('\n\n')
        
        for i in range(0, len_word):

            iterations += 1 # Here Iterations

            if word[i] == char_user:

                correct = 1

                user_word[i] = char_user
            
            else:

                if iterations == len_word and firt_for == 0 and correct == 0:

                    print("Incorrecto")

                    lifes -= 1

            if iterations == len_word:

                firt_for = 0

        for i in user_word:
            print(i, end=' ')

        char_user = input("\nIntroduce una letra: ")

    print("La Palabra era: " + word)

    input("Presiona ENTER para continuar")
