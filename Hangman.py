import random

def generateWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
        return random.choice(words)

wordToGuess = generateWord()

def displayCurrentWords():
    currentRightChoices = ""
    for x in wordToGuess:
        if x in word:
            currentRightChoices += x
        else:
            currentRightChoices += "_"
    return currentRightChoices

def checkwords():
    guessedWord = input("Guess A letter -> ")
    print(f"Word -> {displayCurrentWords()}")

    if not guessedWord.isalpha():
        print("Please use a single letter")
        checkwords()

    if guessedWord in wordToGuess and guessedWord != "":
        word.append(guessedWord)
    
    if guessedWord not in wordToGuess and guessedWord.isalpha():
        print(f"{guessedWord} is not in this word")

def intro():
    print('''
     _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
    print("Welcome to a game of hangman where there is no penalty for being wrong. \nThis version is meant for you to train your brain and help build your vocablulary. Enjoy... :-)\n")

intro()
word = []
generateWord()

while displayCurrentWords() != wordToGuess:
    checkwords()


print(f"You guessed the word '{wordToGuess}' correctly")
