import random
import string
from words import words


def Hangman():
    # print(words)
    word=random.choice(words)
    # word=""
    while "-" in word or " " in word:
        # word.add(words)
        word = random.choice(words).lower()
    print(word)


Hangman()
