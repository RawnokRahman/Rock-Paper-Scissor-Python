import random

# define the choices
choices = ["rock", "paper", "scissors"]

# define the scores
player_score = 0
computer_score = 0

# function to play a round
def play_round():
    global player_score, computer_score  # use global variables
    # get the player's choice
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    while player_choice not in choices:
        player_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ")

    # get the computer's choice
    computer_choice = random.choice(choices)

    # determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("Player wins!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # print the current scores
    print("Player score:", player_score)
    print("Computer score:", computer_score)

# main game loop
while True:
    # play a round
    play_round()

    # ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    while play_again not in ["y", "n"]:
        play_again = input("Invalid input. Do you want to play again? (y/n): ")

    # exit the game if the player doesn't want to play again
    if play_again == "n":
        break

    # reset the scores
    player_score = 0
    computer_score = 0