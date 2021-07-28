#define the word of the game
import random
from words import words_list
def getWord():
    word = random.choice(words_list)
    return word.upper()
#define the parttern of hangman
hangmanParttern = ['''
   +===+
   |   |
   O   |
  /|\  |
  / \  |
       |
   =========''','''
   +===+
   |   |
   O   |
  /|\  |
  /    |
       |
   =========''','''
   +===+
   |   |
   O   |
  /|\  |
       |
       |
   =========''','''
   +===+
   |   |
   O   |
  /|   |
       |
       |
   =========''','''
   +===+
   |   |
   O   |
   |   |
       |
       |
   =========''','''
   +===+
   |   |
   O   |
       |
       |
       |
   =========''','''
   +===+
   |   |
       |
       |
       |
       |
   =========''']
#draw the  gallows
def checkLetters(letter,word):
    indices = []
    for index,eachletter in enumerate(word):
        if eachletter == letter:
            indices.append(index)
    return indices
def game(word):
    tries = 6
    checkWin = False
    guessedLetters = []
    listWord = list(word) # change word from string to list
    showLetters = "_"*len(word)
    showLettersList = list(showLetters)
    showLettersguessed = ""
    print(hangmanParttern[tries])
    print(showLetters)
    while tries > 0 and checkWin == False:
        guess = input("Insert your guessing letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
                if guess in guessedLetters:
                    print("You have guessed this letter, choose other!")
                else:
                    indices = checkLetters(guess,word)
                    if indices == []:
                        guessedLetters.append(guess)
                        tries = tries - 1
                        print(hangmanParttern[tries])
                        print(guess ," is not in the word!", tries, "guess(es) remaining")
                        print("Your past guess(es) are: ",guessedLetters)
                        if showLettersguessed == "":
                            print(showLetters)
                        else:
                            print(showLettersguessed)
                    else:
                        guessedLetters.append(guess)
                        for i in indices:
                            showLettersList[i] = guess
                            showLettersguessed = "".join(showLettersList)
                        print(hangmanParttern[tries])
                        print(guess," is in the word!")
                        print("Your past guess(es) are: ",guessedLetters)
                        print(showLettersguessed)
                        if "_" not in showLettersguessed:
                            checkWin = True
        else:
            print ("This is not a valid letter")
    if checkWin == True:
            print("You win!")
    else:
            print ("Game over! The word is: ",word)
while input("Play? Y/N").upper() == "Y":
    word = getWord()
    game(word)