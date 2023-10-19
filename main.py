# o-rock
# 1-paper
# 2-scissiors 
import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing!")
