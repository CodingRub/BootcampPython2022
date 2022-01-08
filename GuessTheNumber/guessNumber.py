from random import randint
from art import logo

def highOrLowerOrEqual(guess, choose):
    res = False
    if guess > choose:
        print("Your guess is too high")
    elif guess < choose:
        print("Your guess is too low")
    else:
        print("Your guess is correct !")
        res = True
    return res

def life():
    choice = str(input("Choose a difficulty. Type 'easy' or 'hard':\n").lower())
    lifeNbr = 10
    if choice == 'hard':
        lifeNbr = 5
    return lifeNbr

def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    again = True
    while again:
        computer = randint(1, 100)
        lifeNbr = life()
        find = False
        while not find and lifeNbr > 0:
            print(f"You have {lifeNbr} attempts remaining to guess the number.")
            guess = int(input("Make a guess:\n").lower())
            if highOrLowerOrEqual(guess, computer):
                find = True
            else:
                lifeNbr -= 1

        if lifeNbr == 0:
            print(f"You lose to guess the number {computer} ! :(")

        remake = str(input("Restart ?. Type 'y' or 'n':\n").lower())
        if remake == "n":
            print("Goodbye !")
            again = False

if __name__ == "__main__":
    game()
