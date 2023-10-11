import random
from tabulate import tabulate

class Hangman():
    def __init__(self):
        self.food = [
            "cookie", "grapes", "apples",
            "cherries", "chicken", "beef",
            "pork", "cake", "muffin",
            "orange", "cucumber", "banana",
            "beets", "blueberries"
        ]
        self.colors = [
            "red", "orange", "yellow",
            "green", "blue", "violet",
            "black", "white", "turquoise"
        ]
        self.weekdays = [
            "sunday", "monday", "tuesday",
            "wednesday", "thursday", "friday", "saturday"
        ]
        self.errors = 6
        self.attempts = 0
        self.level = ""
        self.catagory = ""
        self.word = ""

    def user_cat(self):
        table = ["Colors", "Food", "Weekdays"]
        while True:
            print("Please choose your catagory!")
            print(tabulate(table[0:], tablefmt = "grid"))
            level = input("Catagory: ").title()
            if level == "Colors":
                self.catagory = self.colors
                break
            elif level == "Food":
                self.catagory = self.food
                break
            elif level == "Weekdays":
                self.catagory = self.weekdays
                break
            else:
                print("Please type a valid catagory")
    def picture(self):
        if self.attempts == 1:
            print("  O  ")
        elif self.attempts == 2:
            print()


    def choose_word(self):
        self.word = random.choice(self.catagory)

    def instructions(self):
        print("Welcome to Hangman")

    def play_game(self):
        self.user_cat()
        self.choose_word()
        self.instructions()
        guessed_word = ["_"] * len(self.word)
        while self.attempts < self.errors:
            print(" ".join(guessed_word))
            guess = input("Guess a word: ").lower()
            if guess.isalpha() and len(guess) == 1:
                if guess in self.word:
                    for _ in range(len(self.word)):
                        if self.word[_] == guess:
                            guessed_word[_] = guess

                    if "_" not in guessed_word:
                        print("Congrats! You guessed the word: ", self.word)
                        break

                else:
                    print("Incorrect guess.")
                    self.attempts += 1
                    print(f"You have {self.errors - self.attempts} attempts left.")

            else:
                print("Please write a single letter.")
        else:
            print(f"You ran out of attempts. Correct word: {self.word}")
