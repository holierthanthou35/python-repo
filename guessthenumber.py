import random
the_num = random.randint(1, 101)
print(the_num)
lives = 0
difficulty = input("what difficulty level do u want? ")
guess = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("invalid input...")

game_end = False


def initiator():
    global lives
    global guess
    # global difficulty
    guess = int(input("what is your guess? "))


def win():
    global guess
    global game_end
    if lives > 0 and guess == the_num:
        print("YOU WON!!!")
        game_end = True


def other_situations():
    global lives
    global game_end
    if guess != the_num and lives > 0:
        if guess > the_num:
            print("too high..")
        else:
            print("too low...")
        lives -= 1
    elif lives == 0:
        print("You LOst...")
        print(f"the number was {the_num}.")
        game_end = True


while not game_end:
    initiator()
    win()
    other_situations()
    print(f"you have {lives} lives left")
