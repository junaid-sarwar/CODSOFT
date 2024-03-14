import random

print("===ROCK PAPER SCISSORS===")

player_score = 0
pc_score = 0
tie = 0

game_choices = ["Rock", "Paper", "Scissors"]

def winner(player_choice, computer_choice):
    if (player_choice == "Rock" and computer_choice == "Paper"):
        print("You Lose!")
        return "pc"
    elif (player_choice == "Rock" and computer_choice == "Scissors"):
        print("YOU WIN :D")
        return "player"
    elif (player_choice == "Scissors" and computer_choice == "Paper"):
        print("YOU WIN :D")
        return "player"
    elif (player_choice == "Scissors" and computer_choice == "Rock"):
        print("You Lose!")
        return "pc"
    elif (player_choice == "Paper" and computer_choice == "Rock"):
        print("YOU WIN :D")
        return "player"
    elif (player_choice == "Paper" and computer_choice == "Scissors"):
        print("You Lose!")
        return "pc"
    else:
        print("TIE!!!, play again")
        return "Tie"

# Loop for starting the game
while True:
    player_choice = input("Pick your choice. Rock, Paper, Scissors: ").capitalize()

    if player_choice not in game_choices:
        print("Please write a valid word.")
        continue

    # Computer chooses random
    computer_choice = random.choice(game_choices)

    # PRINTING THE RESULTS
    print(f"Your Choice: {player_choice}")
    print(f"Computer Choice: {computer_choice}")
    result = winner(player_choice, computer_choice)

    if result == "player":
        player_score += 1
    elif result == "pc":
        pc_score += 1
    else:
        tie += 1
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {pc_score}")
    print(f"Ties: {tie}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break


print("Game Over!")