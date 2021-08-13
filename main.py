from art import logo
import random


def deal_card():
    """ Randomly chooses a card from the card list."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """ Calculates the score of the deck."""

    if sum(cards) == 21 and len(cards) <= 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.append(1)
        cards.remove(11)
    return sum(cards)


def compare(user_score, com_score):
    """ Compares two deck's scores."""
    if user_score > 21 and com_score > 21:
        return "You went over. You lose 😤"

    if user_score == com_score:
        return "Draw 🙃"
    elif com_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif com_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > com_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    com_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        com_score = calculate_score(com_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {com_cards[0]}")

        if user_score == 0 or com_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score <= 17:
        com_cards.append(deal_card())
        com_score = calculate_score(com_cards)

    print(f"    Your cards: {user_cards}, final score: {user_score}\n    Computer cards: {com_cards}, final score: {com_score} ")
    print(compare(user_score, com_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
