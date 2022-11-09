import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6

# n = random.randint(0, len(word_list) - 1)

# chosen_word = str(word_list[n])
chosen_word = random.choice(word_list)

letter_list = []

for i in range(len(chosen_word)):
    letter_list.append(chosen_word[i])

# print(letter_list)
display_list = []
for space in chosen_word:
    display_list += "_"
# print(display_list)
end = False
while not end:

    guess = input("Guess a letter: ").lower()
    # if guess in letter_list:
    for position in range(len(chosen_word)):
        letter = letter_list[position]
        if letter == guess:
            display_list[position] = letter
    print(display_list)

    if guess not in chosen_word:
        lives -= 1
        print(lives)
        print(stages[lives])
        if lives == 0:
            end = True
            print("you lose")
    # if guess in display_list:
    #     print(f"you've already guessed it")
    if "_" not in display_list:
        end = True
        print("YOU won")










