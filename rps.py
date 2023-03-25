import random

while True:
    choices = ["rock", "paper", "scissors"]
    player = input("Pick Rock, Paper, or Scissors: ").lower()
    if player not in choices:
        print("Not an option, choose again:")
    else:
        bot_choice = random.choice(choices)
        print("Bot chose:", bot_choice)

        if player == bot_choice:
            print("It's a tie!")
        elif player == "rock" and bot_choice == "scissors":
            print("You win! Rock beats scissors.")
        elif player == "paper" and bot_choice == "rock":
            print("You win! Paper beats rock.")
        elif player == "scissors" and bot_choice == "paper":
            print("You win! Scissors beats paper.")
        else:
            print("You lose. Better luck next time!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != "y":
            print("Thank you for playing!")
            break