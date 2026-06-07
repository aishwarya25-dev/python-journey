# Guess the number using while loop

import random


while True:
     num = random.randint(1,20)
     Guess = int(input("Guess the no.(1-20): "))


     if Guess == num:
        print("YOU GOT IT MISS\u2764\ufe0f")
        break
     else:
        print("TRY AGAIN")
    