# Making Rock, Paper, Scissors Game

# importing random for making to choose any one from three options
import random

print("-----ROCK, PAPER, SCISSORS-----")
print("-WELCOME TO GAME-")
choice = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice(rock, paper or scissors): ")
    computer_choice = random.choices(choice)

    print("Computer choice: ",computer_choice)

    if computer_choice == user_choice:
         print("It's a tie!!")
    elif ((computer_choice == "rock" and  user_choice == "paper") or 
        (computer_choice == "sicssors" and user_choice == "rock") or
        (computer_choice == "paper" and user_choice == "scissors")):
        print("Ohh yeaaah you wonn!!!")
    else:
        print("Ohhh noo you loose.")
    
    play_again = input("Do you want to play again!!(yes or no): ").lower()

    if play_again != "yes":
        print("Game Over")
    
        break


