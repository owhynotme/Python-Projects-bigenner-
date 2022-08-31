import random
import string


def Hangman():
    word = random.choice(["India", "Skeler", "Eminem", "Skrillex"]).lower()
    print(word)
    valid_words = set(string.ascii_lowercase)
    turns = 7
    guessed_words = ""

    while len(word) > 0:
        main_word = ""

        for letter in word:
            if letter in guessed_words:
                main_word += letter
            else:
                main_word += "_ "

        if main_word == word:
            print("\n")
            print(f" Corect it's {main_word}")
            print("       You Win")
            break

        print("Guess the Letter", main_word)
        guess = input()
        if guess in valid_words:
            guessed_words += guess

        else:
            print("Not a valid Letter")
            guess = input("Enter Letter\n")

        if guess not in word:
            turns -= 1

            if turns == 6:
                print("5 turns left ")

                print("     ----")
                print("    O   |")
                print("        |")

            elif turns == 5:

                print("4 turns left ")

                print("     ----")
                print("    O   |")
                print("    |   |")

            elif turns == 4:

                print("3 turns left ")

                print("     ----")
                print("    O   |")
                print("   /|   |")

            elif turns == 3:

                print("2 turns left ")

                print("     ----")
                print("    O   |")
                print("   /|\  |")

            elif turns == 2:
                print("1 turns left ")

                print("     ----")
                print("    O   |")
                print("   /|\  |")
                print("   /    |")

            if turns == 1:

                print("You lost Nigga")

                print("     ----")
                print("    O   |")
                print("   /|\  |")
                print("   / \  |")

                print("\n  Dead \n")
                break


# name = input("Enter your name\n")
# print("Hello ", name)
Hangman()
