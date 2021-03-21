############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


import random as rand
from bj_logo import logo

main_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    for _ in range(2):
        deck.append(rand.choice(main_deck))
    # deck.append(main_deck[rand.randint(0, 12)])
    return deck


def draw_one_card():
    return rand.choice(main_deck)


def calculate_score(deck):
    # sum = 0
    # for i in range(len(deck)):
    #     sum = sum + deck[i]
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
        return sum(deck)
    return sum(deck)


def compare_score(user_score, computer_score):
    if not user_score > 21 and not computer_score > 21 and user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "Lose, Opponent has blackjack"
    elif user_score > 21:
        return "You lose!! Total more than 21!"
    elif user_score == 0:
        return "Win. You have blackjack"
    elif computer_score > 21:
        return "You win. Opponent went over 21!!"
    elif user_score > computer_score:
        return "You Win!!"
    else:
        return "You lose!!"


def play_blackjack():
    print(logo)
    user_deck = []
    computer_deck = []
    is_game_over = False
    # draw card for user
    user_deck = deal_card(user_deck)
    print(f"Your Deck = {user_deck}")

    # draw card for computer
    computer_deck = deal_card(computer_deck)
    print(f"House Deck = [{computer_deck[0]}]")
    while not is_game_over:
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your cards: {user_deck}, current score: {user_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Enter 'y' to generate another deal. or 'n' to pass.    ").lower()
            if user_deal == 'y':
                user_deck.append(draw_one_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_deck.append(draw_one_card())
        computer_score = calculate_score(computer_deck)

    print(f"   Your final hand: {user_deck}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_deck}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()
