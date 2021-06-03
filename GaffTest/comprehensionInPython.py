numbers = [1, 2, 3, 4, 5]
text = ["One", "Two", "Three", "Four", "Five"]


# List and Dictionary Comprehensions, For-, and If-statements first followed by List and Dictionary Comprehensions
# doing the same thing.

# --- 1. Simple example
print("\n--- Example 1, List Comprehension:")
# For-loop...
result = []
for x in numbers:
    result.append(x)
print(result)

# ...as a List Comprehension...
result_list_comprehension = [x for x in numbers]
print(result_list_comprehension)

# --- 2. Simple example, multiplying x with itself 'x*x'
print("\n--- Example 2:")
# For-loop...
result = []
for x in numbers:
    result.append(x*x)
print(result)

# ...as a List Comprehension...
result = [x*x for x in numbers]
print(result)

# --- 3. Multiplying even-numbered 'x'
print("\n--- Example 3:")
# For and If...
result = []
for x in numbers:
    if x % 2 == 0:
        result.append(x*x)
print(result)

# ...as a List Comprehension...
result = [x*x for x in numbers if x % 2 == 0]
print(result)

# --- 4. Using 'map()' and a lambda function instead.
print("\n--- Example 4, using 'map()' and a lambda function instead of a List Comprehension:")
print(list(map(lambda y: y*y, numbers)))

# --- 5. Nested For-loops.
print("\n--- Example 5 Nested For-loops:")
for num in numbers:
    print(num)
    for t in text:
        print(text)

# ...as a List Comprehension, a List of Lists...
print("List of Tuples: ", [(num, t) for num in numbers for t in text])
print("List of Lists: ", [[num, t] for num in numbers for t in text])
print("List of Dictionaries: ", [{num, t} for num in numbers for t in text])

# --- 6. Simplifying diceRolls.py
print("\n--- Example 6:")
import random
numOfDiceRolled = 6
numSidesOfDice = 10

# For-loop and '.append()'
rollList = []
for roll in range(numOfDiceRolled):
    rollList.append(random.randint(1, numSidesOfDice))

print(rollList)

# ...as a List Comprehension...
rollList = [random.randint(1, numSidesOfDice) for roll in range(numOfDiceRolled)]
print(rollList)

# --- 7. NOT a comprehension in Python. Use of '.get()' instead of 'for, if, dictRolls[rolls] += 1...'.
print("\n--- Example 7 (NOT a comprehension in Python. "
      "Use of '.get()' instead of 'for, if, dictRolls[rolls] += 1...'):")
# For-loop and If-Else statement
dictRolls = {}
for rolls in rollList:
    if rolls in dictRolls:
        dictRolls[rolls] += 1
    else:
        dictRolls[rolls] = 1

print(dictRolls)

# NOT a comprehension in Python. Use of '.get()' instead of 'for, if, dictRolls[rolls] += 1...'.
dictRolls[rolls] = dictRolls.get(rolls, 0) + 1
print(dictRolls)

# --- 8. Flatten a List.
print("\n--- Example 8, Flatten a List:")


# Nested For-loops and '.append()'.
def flatten_long(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


# ...as a List Comprehension...
def flatten(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list


print("Flatten Long: ", flatten_long([[1, 2], [3, 4], [5, 6]]))
print("Flatten with List Comprehension: ", flatten([[1, 2], [3, 4], [5, 6]]))


# --- 9. Dictionary Comprehension.
# Taken from 'https://github.com/programiz/python-best-practices/blob/main/02-comprehension.md'.
print("\n--- Example 9, Dictionary Comprehension:")

# For, If-Else Statements.
pint_price = {"Guinness Foreign Extra": 5, "Punk IPA": 4.5, "Milk": 0.8}

new_price = dict()
for key, value in pint_price.items():
    if value > 2:
        new_price[key] = value * 1.5
    else:
        new_price[key] = value

print(new_price)

# ...as a Dictionary Comprehension...
new_price = {key: value * 1.5 if value > 2 else value for (key, value) in pint_price.items()}
print(new_price)

# --- 10. Dictionary Comprehension.
# Taken from 'https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/'.
print("\nExample 10, Dictionary Comprehension:")
original = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
flipped = {value: key for key, value in original.items()}
print(flipped)
