import random

print("Welcome to Rock-Paper-Scissors Game!")
print("Choices: rock, paper, scissors")

# Get user's choice
user_choice = input("Enter your choice: ").lower()

# Valid choices
choices = ["rock", "paper", "scissors"]

# Check for invalid input
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    exit()

# Computer randomly selects a choice
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "scissors" and computer_choice == "paper") or
    (user_choice == "paper" and computer_choice == "rock")
):
    print("You win!")
else:
    print("Computer wins!")
