# lets play Hangman

import random as rand

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon bat bear camel cat cobra '
             'coyote crow deer dog donkey duck eagle fox frog goat '
             'goose hawk lion lizard llama mole monkey mouse mule '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'swan tiger toad turkey turtle weasel whale wolf '
             'zebra ').split()
lives = 7
reveal_word = []
user_guess = ""
already_guessed = []
end_of_game = False
word_list_length = len(word_list)
chosen_word = word_list[rand.randint(0, word_list_length - 1)]
for _ in chosen_word:
    reveal_word.append("_")

print("Lets play Hangman!!")
print(f"Guess the word:  {reveal_word} \n")

while not end_of_game:
    user_guess = input("Guess a letter:  ").lower()
    letter_count = 0
    if user_guess not in already_guessed:
        already_guessed.append(user_guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == user_guess:
                reveal_word[position] = letter
                letter_count += 1

        if letter_count <= 0:
            lives = lives - 1
            print(f"lives left = {lives}")
            print(stages[6-lives])
        print(reveal_word)

        if lives == 0:
            end_of_game = True
            print("Opps. You ran out of lives. You lost the game!!")
            print(f"The correct answer is '{chosen_word}'")
            print("Better luck Next Time!!")
        if "_" not in reveal_word:
            end_of_game = True
            print("Yaay!! You guessed it correct! You are a winner!!")

    else:
        print(f"You already guessed the letter '{user_guess}'")
        print("Guess a different letter!!")