from data import data
import random
from art import logo, vs

def choiceVs():
    return random.choice(data)

def format_data(account: dict):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def compare(guess, account1, account2):
    res = False
    if account1 > account2:
        res = (guess == "a")
    else:
        res = (guess == "b")
    return res

def game():
    print(logo)
    is_continue = True
    while is_continue:
        score = 0
        account1 = choiceVs()
        account2 = choiceVs()
        playing = True
        while playing:
            print(f"Compare A: {format_data(account1)}.")
            print(vs)
            print(f"Against B: {format_data(account2)}.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            is_correct = compare(guess, account1["follower_count"], account2["follower_count"])
            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                playing = False
                if input("Do you want to continue? Type 'y' or 'n': ") == "n":
                    is_continue = False
                    print("Goodbye !")
            account1 = account2
            account2 = choiceVs()
            while account1 == account2:
                account2 = choiceVs()




if __name__ == "__main__":
    game()