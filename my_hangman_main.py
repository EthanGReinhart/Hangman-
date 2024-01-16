#Making a hangman game on my own
import random

words_list = ['apple', 'banana', 'orange', 'pickle', 'rocket', 'turtle', 'python', 'guitar', 'jacket', 'window',
              'camera', 'purple', 'rabbit', 'pencil', 'summer', 'pocket', 'sunset', 'soccer', 'planet', 'purple']


def get_word():
    word = random.choice(words_list)
    return [*word]


word = get_word()
progress = ['_'] * len(word)



def print_progress(progress):
    for i in progress:
        print(i + ' ', end="")


def guess_letter(word, progress):
    guessed_letters = []
    guess = input("What letter would you like to guess? ")
    if guess.isalpha():
        if guess in word:
            guessed_letters.append(guess)
            print(guessed_letters)
            for i, letter in enumerate(word):
                if guess == letter:
                    progress[i] = guess.upper()
            return progress
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
        round_loop = True
        while round_loop:
            progress = guess_letter(word, progress)
            print(word)
            print_progress(progress)


