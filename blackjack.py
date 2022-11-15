import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
computer_hand = []

start = input("should we start the game? y or n :").lower()

if start == "y":
    cardp1 = cards[random.randint(0, len(cards))]
    cardp2 = cards[random.randint(0, len(cards))]

    player_hand.append([cardp1, cardp2])

    cardc1 = cards[random.randint(0, len(cards))]
    cardc2 = cards[random.randint(0, len(cards))]

    computer_hand.append([cardc1])

    print(f"player's hand {player_hand}")
    print(f"computer's hand {computer_hand}")

    player_hand_sum = sum(player_hand)
    comp_hand_sum = sum(computer_hand)

    if player_hand_sum == 21:
        
    pull = input("do you want to hit or stand? y or n")

    if pull == "y":
        cardp3 = cards[random.randint(0, len(cards))]

        player_hand.append(cardp3)
