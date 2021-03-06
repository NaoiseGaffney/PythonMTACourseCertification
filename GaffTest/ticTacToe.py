# Tic-Tac-Toe in Python 3 to Test Knowledge and Skills
# Created Thursday the 20th and Friday the 21st of May 2021 by Naoise Gaffney - "Gaff"

# Using: dictionaries, nested lists, functions, for-loops, if-else, try-except, nested if statements. Using ANSI
# features, such as colour (red). There is room for improvement of the functionality and code, though works well for a
# first attempt. Please feel free to use and improve.

# Create Tic-Tac-Toe grid using a Dictionary: gridLayout. The values are printed as a numbered grid from 1 to 9, and
# updated with 'X' and 'O' during the game. To check whether a wining combination is played, a list: possibleWins
# defines the possible winning combinations.
gridLayout = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
possibleWins = [["1","2","3"],["4","5","6"],["7","8","9"],["1","4","7"],
                ["2","5","8"],["3","6","9"],["1","5","9"],["3","5","7"]]


def gamesetup():
    """
    gamesetup() prints the title and creates the initial gridLayout numbered from 1 to 9:
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    :return: nothing.
    """
    print("Classic Game of Tic-Tac-Toe or Noughts and Crosses!")
    print(f"     {gridLayout['1']} | {gridLayout['2']} | {gridLayout['3']}\n    ---+---+---\n     {gridLayout['4']}"
          f" | {gridLayout['5']} | {gridLayout['6']}\n    ---+---+---\n     {gridLayout['7']} | {gridLayout['8']}"
          f" | {gridLayout['9']}")
    return


def playgame():
    """
    playgame() sets the initial variables and runs the game (for-loop of 9 iterations (one per play)). If someone has
    won the game ends (break statement), otherwise it checkes whether it is 'X' or 'O' turn to play. Player is asked
    to enter a number from 1 to 9, or 'q' (any other key will work too) to quit. The updated gridLayout is printed.
    checkifwon() is called after 5 iterations (minimum plays to win) to see if there is a winning
    combination.
    :return: nothing.
    """
    count = 0       # count integer is used to decide whether 'X' or 'O' is played (modulo -> even/odd number)
    play = ""       # play string, updated with either cross ('X') or nought ('O')
    cross = "\33[1mX\33[0m"     # Cross 'X', ANSI Code for Bold
    nought = "\33[1mO\33[0m"    # Nought 'O', ANSI Code for Bold
    won = False     # Variable won is False, until checkifwon() updates it to True when someone has won
    maxCount = 9    # Number of iterations for a game of Tic-Tac-Toe

    while count < maxCount:     # 9 iterations, however, is modified if occupied square is selected.
        if won == True:         # If game is won, quit game
            break

        if count % 2 == 0:      # 'X' or 'O' to play
            play = cross
        else:
            play = nought
        count += 1

        chosenNumber = input(f"\33[91m{play}\33[0m to play. Please enter a number from 1 to 9, or 'q' to quit: ")
        try:
            if gridLayout[chosenNumber].isdecimal() and range(1,9):
                gridLayout[chosenNumber] = play
            else:
                print("\33[91mPlease try again, you can't select an already occupied square!\33[0m")
                count -= 1          # Decrease the count integer to ensure the correct turn is set by 'X' or 'O'
        except KeyError:            # 'q' or any other key except the integers 1 to 9 quits the game.
            break

        print(f"     {gridLayout['1']} | {gridLayout['2']} | {gridLayout['3']}\n    ---+---+---\n     {gridLayout['4']}"
              f" | {gridLayout['5']} | {gridLayout['6']}\n    ---+---+---\n     {gridLayout['7']} | {gridLayout['8']}"
              f" | {gridLayout['9']}")
        if count >= 5:              # Call checkifwon() after 5 plays/iterations and above.
            won = checkifwon(play)  # play is either 'X' or 'O'.
    return


def checkifwon(play):
    """
    Iterates through the nested list: possibleWins (winning combinations). If a winning combination is found won = True.
    :param play: play defines whether it is an 'X' or an 'O'
    :return: won is either False (no winning combination yet) or True (one player has won).
    """
    won = False
    for winNumSeries in possibleWins:
        winCount = 0
        if won == False:
            for singleNum in winNumSeries:
                if gridLayout[singleNum] == play:
                    winCount += 1
                    if winCount == 3:
                        won = True
                        print(f"\33[91m{play}\33[0m won!")
    return won

# Calling the main functions to run the game Tic-Tac-Toe. No arguments.
gamesetup()
playgame()