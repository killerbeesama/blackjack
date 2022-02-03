import random 
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_picker(card):
    return random.choice(card)


def add(num):
    total = sum(num)
    if total > 21:
        if 11 in num:
            ace = num.index(11)
            num[ace] = 1 
            total = sum(num)
    return total


def play_game():
    play_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    os.system("cls")
    if play_input == "y":
        print("logo")
        player_card = []
        computer_card = []
        for _ in range(2):
            player_card.append(card_picker(cards))
            computer_card.append(card_picker(cards))

        game_not_over = True
        while game_not_over:
            player_score = add(player_card)
            computer_score = add(computer_card)
            print(f"Your cards: {player_card}, current score: {player_score}")
            print(f"Computer's first card: {computer_card[0]}")
            if computer_score == 21 and len(computer_card) == 2 and player_score == 21 and len(player_card) == 2:
                print("Draw")
                game_not_over = False
            elif computer_score == 21 and len(computer_card) == 2:
                print("You lose opponent has a blackjack")
                game_not_over = False
            elif player_score == 21 and len(player_card) == 2:
                print("You win with a blackjack")
                game_not_over = False
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if another_card == "y":
                    player_card.append(card_picker(cards))
                    player_score = add(player_card)
                    if player_score > 21:
                        print("You went over you lose")
                        game_not_over = False
                elif another_card == "n":
                    while computer_score < 17:
                        computer_card.append(card_picker(cards))
                        computer_score = add(computer_card)

                    if computer_score > 21:
                        print("computer went over you win")
                        game_not_over = False
                    elif computer_score == player_score:
                        print("Draw")
                        game_not_over = False
                    elif computer_score > player_score:
                        print("you lose")
                        game_not_over = False
                    else:
                        print("you win")
                        game_not_over = False        
                else:
                    print("Type a valid keyword to continue or end")                
        
        print(f"Your final hand: {player_card}, final score: {player_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        play_game()
    elif play_input == "n":
        pass
    else:
        print("Please type in a valid input 'y' or 'n'")

play_game()