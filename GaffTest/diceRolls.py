# Created 'diceRolls.py', to roll an 'n'-sided die 'x' times, provide roll statistics, and a 'forLucaTest()' function
# to award points to dice roll values.

import random

numSidesOfDice = 0
numOfDiceRolled = 0

def rollDice(numSidesOfDice, numOfDiceRolled):
    rollList = []
    for roll in range(numOfDiceRolled):
        rollList.append(random.randint(1,numSidesOfDice))

    return rollList

def inputDice():
    try:
        numSidesOfDice = int(input("Please enter the number of sides to your dice: ").strip())
        numOfDiceRolled = int(input(f"Please enter the number of {numSidesOfDice} to roll: ").strip())
    except ValueError:
        print("Please enter only numbers!")
        exit(-1)

    return numSidesOfDice, numOfDiceRolled

def statistics(rollListResults):
    print("Roll Results: ", rollListResults)
    print("Largest dice roll: ", max(rollListResults))
    print("Lowest dice roll: ", min(rollListResults))
    print("Sum of dice roll(s): ", sum(rollListResults))

    dictRolls = {}
    dictInRightOrder = {}
    for rolls in rollListResults:
        if rolls in dictRolls:
            dictRolls[rolls] += 1
        else:
            dictRolls[rolls] = 1
    tuple_in_right_order = sorted(dictRolls.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    return tuple_in_right_order

def forLucaTesta(statisticsTupleOrderedResults):
    for value in statisticsTupleOrderedResults:
        print(f"Dice roll: {value[0]}, Number of times rolled: {value[1]}, Points scored:"
              f" {value[1]} * 1000 = {value[1]*1000} ")

# Call Dice Functions
numSidesOfDice, numOfDiceRolled = inputDice()
rollListResults = rollDice(numSidesOfDice, numOfDiceRolled)
statisticsTupleOrderedResults = statistics(rollListResults)
forLucaTesta(statisticsTupleOrderedResults)