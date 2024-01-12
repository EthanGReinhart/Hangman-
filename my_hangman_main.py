#Making a hangman game on my own
import random

words_list = ['apple', 'banana', 'orange', 'pickle', 'rocket', 'turtle', 'python', 'guitar', 'jacket', 'window',
              'camera', 'purple', 'rabbit', 'pencil', 'summer', 'pocket', 'sunset', 'soccer', 'planet', 'purple']

def get_word():
    word = random.choice(words_list)
    return [*word]

def print_word(word):
    word_as_list = ['_'] * len(word)
    for i in word_as_list:
        print(i + ' ', end="")


def guess_letter(word):
    guessed_letters = []
    guess = input("What letter would you like to guess? ")
    word_as_list = ['_'] * len(word)
    if guess.isalpha():
        if guess in word:
            guessed_letters.append(guess)
            print(guessed_letters)
            for i, letter in enumerate(words_list):
                if guess == letter:
                    word_as_list[i] = guess.upper()
            return word
        else:
            print("Letter not in word")
            guessed_letters.append(guess)
            print(guessed_letters)

    else:
        print("Your guess must be a letter")

run = True
while run:
    will_play = input("\nWould you like to play? (Y/N) ")
    if will_play.lower() == "y":
        word = get_word()
        guess_letter(word, words_list)
        print(word)
        print_word(word)


