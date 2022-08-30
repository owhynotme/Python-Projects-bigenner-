import random


def guess(x):
    random_number = random.randint(1, x)
    # print(random_number)
    num = 0
    while int(random_number) != int(num):
        num = input(f"Enter Number b/w 1-{x}\n")
        if int(num) < int(random_number):
            print("Number is Smol\n")
        elif int(num) > int(random_number):
            print("Number is big\n")

        # n += 1
    print("You guessed it correct")


guess(10)
