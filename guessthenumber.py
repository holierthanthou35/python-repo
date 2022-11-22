import random
the_num = random.randint(1, 101)

difficulty = input("what difficulty do you want to play in 'easy' or 'hard': ")
guess = int(input("what is your guess?: "))
game_end = False

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5


def check():
    global lives
    global game_end
    if guess == the_num:
        print("you won!!!")
        game_end = False

    elif guess != the_num:
        if guess > the_num:
            print("Too High!! try again...")
        elif guess < the_num:
            print("Too Low!! try again")
    lives -= 1


if lives == 0:
    game_end = True

#check()
while not game_end:
    check()