# Write loop for game rock scissors paper game
# 1. Ask user to input rock, scissors or paper
# If user input is not rock, scissors or paper, ask user to input again and don't proceed
# 2. Generate random choice for computer
# 3. Compare user choice and computer choice
# 4. Print the result of the game
# 5. Ask user if they want to play again
# If yes, repeat the game
# If no, exit the game

import random

while True:
    user_choice = input("Enter rock, scissors, or paper: ")
    
    if user_choice not in ["rock", "scissors", "paper"]:
        print("Invalid input. Please try again.")
        continue
    
    computer_choice = random.choice(["rock", "scissors", "paper"])
    
    print("User choice:", user_choice)
    print("Computer choice:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
    
    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() != "yes":
        break