# Number guessing using random module and while loop

import random

guess = random.randint(1, 10)

while True:
    num = int(input("Guess the number(1-10): "))

    if num == guess:
        print("You guss it right!!")
        break
    elif num > guess:
        print("Too high")
    else:
        print("Too low")