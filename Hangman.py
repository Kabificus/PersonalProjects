import random

library = ['aids', 'table', 'how', 'learn', 'drift', 'but', 'purse', 'stand', 'yet', 'set', 'music', 'me', 'house', 'could', 'among', 'oh', 'as', 'their', 'piqued', 'our', 'sister', 'shy', 'nature', 'almost', 'his', 'wicket', 'hand', 'dear', 'so', 'we', 'hour', 'to', 'he', 'we', 'be', 'hastily', 'offence', 'effects', 'he', 'service', 'sympathize', 'it', 'projection', 'ye', 'insipidity', 'celebrated', 'my', 'pianoforte', 'indulgence', 'Point', 'his', 'truth', 'put', 'style', 'elegance', 'exercise', 'as', 'laughing', 'proposal', 'mistaken', 'if', 'We', 'up', 'precaution', 'an', 'it', 'solicitude', 'acceptance', 'invitation']
# file = 'Hangman.txt'
# library = open(file).read().split()
guessedLetters = []
correct = 0

def start():
    del guessedLetters[:]
    StartGame = input("Start game or add word? (quit to quit)").lower()
    if StartGame == 'start':
        run_game()
    elif StartGame == 'add':
        newWord = input("What is the new word you would like to add?").lower()
        if check(newWord, library) == False:
            appendLibrary(newWord)
            print(library)
            start()
        elif check(newWord, library) == True:
            print('That word already exists in our dictionary')
            start()
    elif StartGame == 'quit':
        quit()
    else:
        print("Your input is unknown, try again")
        start()

def check(word, library):
    if word in library:
        return(True)
    else:
        return(False)


def run_game():
    mysteryWord = random.choice(library)
    chances = len(mysteryWord)+1
    print('The mystery word has', len(mysteryWord), 'letters')
    print('You can make', chances, 'mistakes')
    for i in mysteryWord:
        print('_', end=' ')
    print()
    guess_letter(mysteryWord, chances)

def guess_letter(word, chances):
    correct = 0
    tempChance = False
    guess = input('Guess a letter:')
    if len(guess) == 1:
        if check(guess, guessedLetters) == False:
            guessedLetters.append(guess)
            for g in word[::1]:
                if g == guess:
                    tempChance = True
                if g in guessedLetters:
                    print(g, end=" ")
                    correct += 1
                else:
                    print('_', end=" ")
            print()
            if tempChance == False:
                chances -= 1
                print('There are no', guess, "'s")
        else:
            print("That letter has already been guessed!")
    elif len(guess) == len(word):
        if guess == word:
            print("Congrats, you guessed the word")
            start()
        else:
            print("Sorry, that's not the word")
            chances -= 1
            if chances == 0:
                print('You lose the game!')
                start()
            print('You can make', chances, 'more mistakes')
            guess_letter(word, chances)
    print(correct, 'letter(s) so far')
    print('You can make', chances, 'more mistakes')
    if correct == len(word):
        print('Congrats you won!')
        start()
    if chances == 0:
        print('You lose the game!')
        start()
    guess_letter(word, chances)


def appendLibrary(word):
    with open(file, 'a') as myfile:
        myfile.write(' ')
        myfile.write(word)
        myfile.close()


start()