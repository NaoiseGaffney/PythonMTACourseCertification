# Die/dice rolls in Python 3 to Test Knowledge and Skills
# Created Saturday the 22nd of May 2021 by Naoise Gaffney - "Gaff"

# Using: functions, try-except, for loops, if-else, and a lambda function. Dictionaries, lists, and tuples.
# There is room for improvement of the functionality and code, though works well for a first attempt.
# Please feel free to use and improve.

# Created 'diceRolls.py', to roll an 'n'-sided die 'x' times, provide roll statistics, and a 'forLucaTesta()' function
# to award points to die roll values.

import random

# Global variables for the die size and number of dice rolled.
numSidesOfDice = 0
numOfDiceRolled = 0


def inputDice():
    """
    Asks for user input, numberf of sides of the die, and number of dice rolled.
    Called with 'numSidesOfDice, numOfDiceRolled = inputDice()'
    abs() returns positive numbers only (-4 -> 4), int() converts the text string to integer, and strip() removes
    whitespace before and after the integer.
    Try-except wraps the input() and catches the ValueError (if anything but whole numbers (integres) are entered.
    exit(-1) quits the application if ValueError occurs (-1 = ErrorLevel 255).
    :return numSidesOfDice, numOfDiceRolled: the size of the die, and the number of dice.
    """
    try:
        numSidesOfDice = abs(int(input("Please enter the number of sides to your dice: ").strip()))
        numOfDiceRolled = abs(int(input(f"Please enter the number of {numSidesOfDice} to roll: ").strip()))
    except ValueError:
        print("Please enter only numbers!")
        exit(-1)

    return numSidesOfDice, numOfDiceRolled


def rollDice(numSidesOfDice, numOfDiceRolled):
    """
    Rolls 'n'-sided die (numSidesOfDice) 'x' number of time (numOfDiceRolled).
    Called with 'rollListResults = rollDice(numSidesOfDice, numOfDiceRolled)'
    :param numSidesOfDice: determines the die size (die number).
    :param numOfDiceRolled: determines the number of dice rolled.
    :return rollList: Contain the list of rolled dice results.
    """
    rollList = []
    for roll in range(numOfDiceRolled):
        rollList.append(random.randint(1,numSidesOfDice))

    return rollList


def statistics(rollListResults):
    """
    Prints die roll statistics based on the results of the die rolls.
    Called with 'statisticsTupleOrderedResults = statistics(rollListResults)'
    :param rollListResults: rollDice() provides the results of the die rolls.
    :return tuple_in_right_order: rollListResults are sorted in descending value (number of die
    roll occurences, for example rolling a 6-sided die with the result of 5 rolled 10 times out of 20 rolls, will sort
    the results by the 10 times the 5 was rolled).
    - The rolls are saved to a dictionary and the value (occurences)
    incremented after each occurence.
    - The lambda function sorts the key, value by descending (reverse=True)
    order.
    - The previous statistics use common Python functions like max(), min(), and sum().
    """
    print("Roll Results: ", rollListResults)
    print("Largest dice roll: ", max(rollListResults))
    print("Lowest dice roll: ", min(rollListResults))
    print("Sum of dice roll(s): ", sum(rollListResults))

    dictRolls = {}
    for rolls in rollListResults:
        if rolls in dictRolls:
            dictRolls[rolls] += 1
        else:
            dictRolls[rolls] = 1
    tuple_in_right_order = sorted(dictRolls.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    return tuple_in_right_order

def forLucaTesta(statisticsTupleOrderedResults):
    """
    Calculates the value of the die rolls, '{value[1]*1000}'.
    :param statisticsTupleOrderedResults: provides the Tuple of die rolls and their occurences (number of times rolled).
    :return: None.
    """
    for value in statisticsTupleOrderedResults:
        print(f"Dice roll: {value[0]}, Number of times rolled: {value[1]}, Points scored:"
              f" {value[1]} * 1000 = {value[1]*1000} ")


# Call Dice Functions
numSidesOfDice, numOfDiceRolled = inputDice()               # User input, die size, and number of dice.
rollListResults = rollDice(numSidesOfDice, numOfDiceRolled) # The results of the die rolls based on inputDice().
statisticsTupleOrderedResults = statistics(rollListResults) # Die roll statistics.
forLucaTesta(statisticsTupleOrderedResults)                 # Special function for Luca Testa to calculate values.