from random import choice
from art import logo

def cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def main():
    cardsPlayer = [cards() for i in range(2)]
    cardsComputer = [cards() for i in range(2)]
    is_game_over = False
    print(logo)
    while not is_game_over:
        user_score = calculate_score(cardsPlayer)
        computer_score = calculate_score(cardsComputer)
        print(f"Your cards: {cardsPlayer}, current score: {user_score}")
        print(f"Computer's first card: {cardsComputer[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                cardsPlayer.append(cards())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        cardsComputer.append(cards())
        computer_score = calculate_score(cardsComputer)
    
    print(f"   Your final hand: {cardsPlayer}, final score: {user_score}")
    print(f"   Computer's final hand: {cardsComputer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    main()