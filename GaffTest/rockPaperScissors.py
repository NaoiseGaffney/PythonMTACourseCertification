# Importing 'random' library to use 'randint()' for the computer rock, paper, scissors choices.
import random

# 'win_list[]' contains the winning combinations for the player. Anything else is a loss or a draw if choices are equal.
# 'rps_list[]' contains the choices for the computer, based on the random number index of 0 to 2.
# 'player_rps' is the string variable for the player's choice.
# 'draws = wins = losses = 0', sets all three variables to the Integer 0. Used for game statistics.
win_list = [["rock '()'", "scissors 'db'"], ["paper '[]'", "rock '()'"], ["scissors 'db'", "paper '[]'"]]
rps_list = ["rock '()'", "paper '[]'", "scissors 'db'"]
player_rps = ""
draws = wins = losses = 0

# While-loop continues until player selects 'q' to quit.
while player_rps != "q":
    computer_rps = random.randint(0, 2)     # Random number from 0 to 2, rps_list[] index.
    computer_rps = rps_list[computer_rps]   # Save "rock '()'" or "paper '[]'" or "scissors 'db'" string.
    # Ask for player input. Remove whitespaces 'strip()' and convert all entries to lower-case 'lower()'.
    player_rps = input("\nPlease enter 'r = rock' or 'p = paper' or 's = scissors' or q to quit: ").strip().lower()
    # Player choice is set to full string for later comparison with the computer's random choice.
    # 'q' for quit, printing end-of-game statistics.
    # Handles any incorrect entries, and sets 'player_rps = False' to check later on so as to skip the evaluations.
    if player_rps == "r":
        player_rps = "rock '()'"
    elif player_rps == "p":
        player_rps = "paper '[]'"
    elif player_rps == "s":
        player_rps = "scissors 'db'"
    elif player_rps == "q":
        print(f"Game statistics for this round:\nPlayer => Wins: {wins}, Draws: {draws}, Losses: {losses}.")
        exit(-1)
    else:
        print("Please try again!")
        player_rps = False      # Set 'player_rps' to False to ensure no evaluation is performed -> While-loop.

    # Evaluations. First check to see that an incorrect entry/input was made, then evaluate draw or win or loss.
    if player_rps != False:     # If player entered an incorrect choice, 'player_rps' is False. Skip next code block.
        if player_rps == computer_rps:                  # If both are equal (same choice), it's a draw.
            draws += 1      # Add 1 to draws for statistics.
            print(f"A draw! :-| You played {player_rps}, and the computer played {computer_rps}.")
        elif [player_rps, computer_rps] in win_list:    # If player has a winning combination, it's a win.
            wins += 1       # Add 1 to wins for statistics.
            print(f"You won! :-) You played {player_rps}, and the computer played {computer_rps}.")
        else:                                           # If neither a draw or a win, it's a loss.
            losses += 1     # Add 1 to losses for statistics.
            print(f"You lost! :-( You played {player_rps}, and the computer played {computer_rps}.")