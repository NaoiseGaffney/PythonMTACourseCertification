# Created a simple die roll app for a friend, to explain fundamantal programming concepts.

# Importing the random library to create random numbers from 1 to 6 using 'random.randint(1, 6)'
import random

# Creating variables to hold the number of die rolls per number of a six-sided die. All set to 0.
six = 0                                 # Variable 'six' to store the number of times a six is rolled
five = 0                                # Variable 'six' to store the number of times a five is rolled
four = 0                                # Variable 'six' to store the number of times a four is rolled
three = 0                               # Variable 'six' to store the number of times a three is rolled
two = 0                                 # Variable 'six' to store the number of times a two is rolled
one = 0                                 # Variable 'six' to store the number of times a one is rolled
awardPoints = 0                         # Variable 'awardPoints' to store the points awarded to a roll combination

# A for-loop to roll a six-sided die six times.
for roll in range(6):                   # For-loop to roll the die 6 times.
    dieRoll = random.randint(1, 6)      # Roll the die and save the result in 'dieRoll'
    if dieRoll == 6:                    # If the die roll result is 6...
        six += 1                        # Add one to the number six
    elif dieRoll == 5:                  # If the die roll result is 5...
        five += 1                       # Add one to the number five
    elif dieRoll == 4:                  # If the die roll result is 4...
        four += 1                       # Add one to the number four
    elif dieRoll == 3:                  # If the die roll result is 3...
        three += 1                      # Add one to the number three
    elif dieRoll == 2:                  # If the die roll result is 2...
        two += 1                        # Add one to the number two
    else:                               # If the die roll result is not 6, 5, 4, 3, 2, it must be 1...
        one += 1                        # Add one to the number one

print(f"Die rolls - One: {one}, Two: {two}, Three: {three}, Four: {four}, Five: {five}, Six: {six}")

# Award points to die rolls of 3 or more.
# Check sixes first. Six sixes? No, then five sixes? No, then four sixes? No, then three sixes?
if six == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 sixes! We award you 1,000,000 points!")
elif six == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 sixes! We award you 100,000 points!")
elif six == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 sixes! We award you 10,000 points!")
elif six == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 sixes! We award you 1,000 points!")

# Check fives next. Six fives? No, then five fives? No, then four fives? No, then three fives?
if five == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 fives! We award you 1,000,000 points!")
elif five == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 fives! We award you 100,000 points!")
elif five == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 fives! We award you 10,000 points!")
elif five == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 fives! We award you 1,000 points!")

# Check fours next. Six fours? No, then five fours? No, then four fours? No, then three fours?
if four == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 fours! We award you 1,000,000 points!")
elif four == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 fours! We award you 100,000 points!")
elif four == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 fours! We award you 10,000 points!")
elif four == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 fours! We award you 1,000 points!")

# Check threes next. Six threes? No, then five threes? No, then four threes? No, then three threes?
if three == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 threes! We award you 1,000,000 points!")
elif three == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 threes! We award you 100,000 points!")
elif three == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 threes! We award you 10,000 points!")
elif three == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 threes! We award you 1,000 points!")

# Check twos next. Six twos? No, then five twos? No, then four twos? No, then three twos?
if two == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 twos! We award you 1,000,000 points!")
elif two == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 twos! We award you 100,000 points!")
elif two == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 twos! We award you 10,000 points!")
elif two == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 twos! We award you 1,000 points!")

# Check ones next. Six ones? No, then five ones? No, then four ones? No, then three ones?
if one == 6:
    awardPoints += 1000000
    print(f"Congratulations, you have 6 ones! We award you 1,000,000 points!")
elif one == 5:
    awardPoints += 100000
    print(f"Congratulations, you have 5 ones! We award you 100,000 points!")
elif one == 4:
    awardPoints += 10000
    print(f"Congratulations, you have 4 ones! We award you 10,000 points!")
elif one == 3:
    awardPoints += 1000
    print(f"Congratulations, you have 3 ones! We award you 1,000 points!")

# Print the total points awarded.
print(f"You are awarded a total of {awardPoints:,d} points!")
