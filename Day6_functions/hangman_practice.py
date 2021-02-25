# generate a random word
# display the random word with "_"
# based on user guess, fill the blanks with correct values
# every incorrect entry will involve a reduction in life.
# total incorrect guesses allowed is only 6

import random as rand

word_list = ["random", "pineapple", "camel"]

# Randomly choose a word from the list
# Ask user to guess a letter
# check if the letter is available in the chosen word
# and print Right/Wrong for every letter in the word

word_list_length = len(word_list)
chosen_word = word_list[rand.randint(0, word_list_length - 1)]

# easy way
# chosen_word = rand.choice(word_list)

print("_ " * len(chosen_word))

#
# user_guess = input("Guess a letter:  ").lower()
#
# for letter in chosen_word:
#     if user_guess == letter:
#         print("Right ")
#     else:
#         print("Wrong")

# print the word as _ indicating every letter
# reveal the correct letter if chosen by user and keep the others empty

reveal_word = []
for _ in chosen_word:
    reveal_word.append("_")


print(reveal_word)
user_guess = input("Guess a letter:  ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == user_guess:
        reveal_word[position] = letter

print(reveal_word)


