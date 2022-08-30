import random


def play():
    computer = random.choice(['r', 'p', 's'])
    print(computer)
    user = input("Enter your choice R (rock) P (paper) S (siccior)\n").lower()

    if user == computer:
        return 'Tie'

    # r>s s>p p>r
    if is_won(user, computer):
        return 'You win'

    return 'You Lose'


def is_won(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True


print(play())
