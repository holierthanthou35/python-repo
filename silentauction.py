import os
bid_list = []
bid_count = True

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


def bid_winner(bidding_rec):
    highest_bid_amount = 0
    winner = ""
    for bidder in bidding_rec:
        bid_amount = bidding_rec[bidder]
        if bid_amount > highest_bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid_amount}")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


while bid_count:
    bids_dict = {}

    input_name = input("what is your name?")
    input_bid = int(input("what is your bid?"))

    bids_dict[input_name] = input_bid

    bidders = input("are there any more bidders in the room?")
    if bidders == "yes":
        cls()
    elif bidders == "no":
        bid_count = False
        bid_winner(bids_dict)
    else:
        print("answer in yes or no.")

