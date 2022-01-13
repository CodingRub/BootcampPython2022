from random import choice, randint, shuffle
import string


def pwdGen() -> str:
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    numbers = []
    for i in range(10):
        numbers.append(i)
    symbols = ['!', '#', '%', '&', '$', '(', ')', '*', '+']
    res = []
    for i in range(randint(6, 8)):
        res.append(choice(alphabet))
    for i in range(randint(2, 4)):
        res.append(choice(symbols))
    for i in range(randint(2, 4)):
        res.append(str(choice(numbers)))
    shuffle(res)
    return ''.join(res)