class Hangman:
    def __init__(self):
        self.words_list = ['apple', 'banana', 'orange', 'pickle', 'rocket',
              'turtle', 'python', 'guitar', 'jacket', 'window',
              'camera', 'purple', 'rabbit', 'pencil', 'summer',
              'pocket', 'sunset', 'soccer', 'planet', 'purple']

        self.word = self.get_word()
        self.wrong_guesses = []
        self.progress = ["_"] * len(self.word)

    def get_word(self):
        return self.words_list[random.randint(0, len(self.words_list) -1)]

    def get_input(self):
        guess = input("Guess A Letter")
        return guess

    def print_guesses(self):
        if len(self.wrong_guesses) > 0:
            for char in self.wrong_guesses:
                print(char, end=", ")
            print()
        else:
            print("No Wrong Guesses")

    def print_menu(self):
        print("Welcome to Python Hangman!\n"
              "You have 6 tries to correctly guess the word")

    def print_progress(self):
        for element in self.progress:
            print(element, end = " ")
        print()

    def update_hangman(self, guess):
        if guess in self.word:
            for count, char in enumerate(self.word):
                if guess == char:
                    self.progress[count] = guess
        else:
            self.wrong_guesses += guess


    def check_win(self):
        if len(self.wrong_guesses) == 6:
            if "".join(self.progress) == self.word:
                print("You Win!\n")
            else:
                print("You Lose!")
                print(f"The word was {self.word}\n")
            round_loop = False

        elif len(self.wrong_guesses) < 6:
            if "".join(self.progress) == self.word:
                print("You Win!\n")
                round_loop = False
            else:
                return True

        return round_loop

def main():
    game_loop = True
    while game_loop:

        round_loop = True
        game = Hangman()
        game.print_menu()
        print(f"\nYour word is: ", end="")

        while round_loop:

            game.print_progress()
            print(f"\nWrong Guesses: ", end="")
            game.print_guesses()
            player_guess = input("Guess a character: ")
            game.update_hangman(player_guess)
            round_loop = game.check_win()


if __name__ == "__main__":
   main()