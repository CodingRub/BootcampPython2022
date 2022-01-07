from random import *
from hangman_words import word_list
from hangman_art import stages, logo

def genRndWord(words: list) -> str:
    print("Generating the word")
    return list(choice(words).lower())

def genBlank(word: str) -> list:
    blank = []
    for i in range(len(word)):
        blank.append("_")
    return blank

def findBlank(word: list, blank: list) -> bool:
    res = ""
    if blank == word:
        res = f"Congratulations! You have found the word {''.join(word)}"
    else:
        res = f"You have no more lives, the word was {''.join(word)}"
    return res

def hangmanForLife(stages: list, life: int) -> str:
    res = ""
    for i in range(len(stages)):
        if life == i:
            res = stages[i]
    return res

def main(stages = stages) -> None:
    print(logo)
    print("Welcome to the Hangman Game !")
    print("I choose a word and you have to find it, okay?")
    word = genRndWord(word_list)
    word_copy = word.copy()
    blank = genBlank(word)
    life = 5
    print(''.join(blank))
    while '_' in blank and life > 0:
        letter = str(input("Choose a letter ! ").lower())
        if letter in word:
            blank[word.index(letter)] = letter
            word[word.index(letter)] = "_"
        else:
            print("Oh no ! The letter is not in the word")
            life -= 1
        print(hangmanForLife(stages, life))
        print(''.join(blank))
    print(findBlank(word_copy, blank))


if __name__ == '__main__':
    main()