import random


def pc_guess(x):
    low = 1
    high = x
    feedback = ""
    while(feedback != "c"):
        randnum = random.randint(low, high)
        feedback = input(f"{randnum} C (correct) H (high) L (low)\n").lower()
        if feedback == "h":
            high -= 1
        elif feedback == "l":
            low += 1

    print("Correct")


pc_guess(10)
