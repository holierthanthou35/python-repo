import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def cardgen(card_list):
    card = random.choice(cards)
    card_list.append(card)


player_hand = []
# player_score = sum(player_hand)
computer_hand = []
# comp_score = sum(computer_hand)
end = False

while not end:
    start = input("should we start the game? y or n: ").lower()
    if start == "y":
        cardgen(player_hand)
        cardgen(player_hand)
        print(player_hand)

        cardgen(computer_hand)
        print(computer_hand)

        if sum(player_hand) == 21:
            print('YOU WON!!!')
            end = True
        else:
            end_2 = False
            while not end_2:
                hit_or_stand = input("Do you want to hit or stand? ")

                if hit_or_stand == "hit":
                    cardgen(player_hand)
                    print(player_hand)

                    if sum(player_hand) > 21:
                        print("This is a BUST!!!")
                        end = True
                        end_2 = True

                    elif sum(player_hand) == 21:
                        print('YOU WON!!!')
                        end = True
                        end_2 = True

                elif hit_or_stand == "stand":
                    cardgen(computer_hand)
                    print(player_hand)

                    print(computer_hand)

                    if sum(player_hand) > sum(computer_hand):
                        print("YOU WON!!!")
                        end = True
                        end_2 = True

                    elif sum(player_hand) < sum(computer_hand):
                        print("Dealer wins")
                        end = True
                        end_2 = True

                    else:
                        print("this is a draw.")
                        end = True
                        end_2 = True

                else:
                    print("Try typing 'hit' or 'stand' to continue game.")

    elif start == "n":
        end = True

    else:
        print("Try a valid input")

