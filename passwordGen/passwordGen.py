import random
from random import *
import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = []
for i in range(10):
    numbers.append(i)
symbols = ['!', '#', '%', '&', '$', '(', ')', '*', '+']

def pwdGen(letters: list, numbers: list, symbols: list) -> str:
    res = []
    if type(letters) == list and type(numbers) == list and type(symbols) == list:
        print("Welcome to the PyPassword Gen !")
        nb_letters = int(input('How may letters in the password ? '))
        nb_symbols = int(input('How may symbols in the password ? '))
        nb_numbers = int(input('How may numbers in the password ? '))
        for i in range(1, nb_letters + 1):
            res.append(choice(alphabet))
        for i in range(1, nb_symbols + 1):
            res.append(choice(symbols))
        for i in range(1, nb_numbers + 1):
            res.append(str(choice(numbers)))
        shuffle(res)
    else:
        raise ValueError("pwdGen() : Il faut que les paramètres mit soient de type List !")
    return ''.join(res)

print(pwdGen(alphabet, numbers, "5"))