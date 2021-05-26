# https://pythonprinciples.com/

# 1. ----- * ----- * ----- 2/10 ----- * ----- * ----- Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
print("\n1. ----- * ----- * ----- 2/10 ----- * ----- * ----- Capital indexes\n")
def capital_indexes(string):
    capitalList = []
    counterIndex = 0
    for character in string:
        if character.isupper():
            capitalList.append(counterIndex)
        counterIndex += 1
    return capitalList

capitalList = capital_indexes("Naoise Olof Seán Gaffney")
print("Capital List 1, using a 'counterIndex = 0'\n", capitalList)

# Second example using Enumerate
def capital_indexesEnumerate(string):
    capitalList = []
    for counter, character in enumerate(string):
        if character.isupper():
            capitalList.append(counter)
    return capitalList

capitalList = capital_indexesEnumerate("Naoise Olof Seán Gaffney")
print("Capital List 2, using a 'for counter, character in enumerate(string):'\n", capitalList)

"""
# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]
"""

# 2. ----- * ----- * ----- 2/10 ----- * ----- * ----- Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle
# letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
print("\n2. ----- * ----- * ----- 2/10 ----- * ----- * ----- Middle letter\n")
def mid(string):
    if len(string) % 2 == 0:
        return ""
    else:
        return string[(len(string) // 2)]


middleCharacter = mid("Six")
print(middleCharacter)

# 3. ----- * ----- * ----- 2/10 ----- * ----- * ----- Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
#
# For example, consider the following dictionary:
#
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
#
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of
# names to the string "online" or "offline", as seen above.
#
# Your function should return the number of people who are online.
print("\n3. ----- * ----- * ----- 2/10 ----- * ----- * ----- Online status\n")
def online_count(dictionary):
    counter = 0
    for value in dictionary.values():
        if value == "online":
            counter += 1
    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

counterResult = online_count(statuses)
print(counterResult)

"""
# short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])
"""

# 4. ----- * ----- * ----- 2/10 ----- * ----- * ----- Randomness
# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and
# 100, both inclusive, and return it.
# Calling the function multiple times should (usually) return different numbers.
# For example, calling random_number() some times might first return 42, then 63, then 1.
print("\n4. ----- * ----- * ----- 2/10 ----- * ----- * ----- Randomness\n")
import random

def random_number():
    return random.randint(1,100)

print(random_number())

# 5. ----- * ----- * ----- 2/10 ----- * ----- * ----- Type check
# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are
# integers, and False otherwise.
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
print("\n5. ----- * ----- * ----- 2/10 ----- * ----- * ----- Type check\n")
def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False

print(only_ints('a', 4))
"""
# Short answer
def only_ints(a, b):
    return type(a) == int and type(b) == int
"""

# 6. ----- * ----- * ----- 3/10 ----- * ----- * ----- Double letters
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a
# row.
# Define a function named double_letters that takes a single parameter. The parameter is a string.
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.
print("\n6. ----- * ----- * ----- 3/10 ----- * ----- * ----- Double letters\n")
def double_letters(string):
    double = False
    for character in range(len(string) - 1):
        if string[character] == string[character + 1]:
            double = True
    return double

print(double_letters("nonno"))
"""
# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
"""

# 7. ----- * ----- * ----- 3/10 ----- * ----- * ----- Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling
# add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
# For example, calling remove_dots("t.e.s.t") should return "test". If both functions are correct, calling
# remove_dots(add_dots(string)) should return back the original string for any string.
# (You may assume that the input to add_dots does not itself contain any dots.)
print("\n7. ----- * ----- * ----- 3/10 ----- * ----- * ----- Adding and removing dots\n")
def add_dots(string):
    newString = ""
    for count, character in enumerate(string):
        if count == len(string) - 1:
            newString += character
        else:
            newString += character + "."
    print(newString)
    return newString


def remove_dots(string):
    originalString = ""
    for character in string:
        if character == ".":
            pass
        else:
            originalString += character
    return originalString


print(remove_dots(add_dots("Test")))

"""
# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
"""

# 8. ----- * ----- * ----- 3/10 ----- * ----- * ----- Counting syllables
# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a
# single word divided into syllables by hyphens, such as these:
#
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
#
# For example, the call count("ho-tel") should return 2.
print("\n8. ----- * ----- * ----- 3/10 ----- * ----- * ----- Counting syllables\n")

def count(string):
    return len(string.split("-"))


print(count("ho-tel"))

# 9. ----- * ----- * ----- 3/10 ----- * ----- * ----- Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the
# strings are anagrams, and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob")
# should return False.
print("\n9. ----- * ----- * ----- 3/10 ----- * ----- * ----- Anagrams\n")


def is_anagram(string1, string2):
    dictString1 = string2Dict(string1)
    dictString2 = string2Dict(string2)
    if dictString1 == dictString2:
        return True
    else:
        return False


def string2Dict(string):
    dictString = {}
    for character in string:
        if character in dictString:
            dictString[character] += 1
        else:
            dictString[character] = 1
    print(dictString)
    return dictString


print(is_anagram("listens", "silents"))


# easy solution
print("\nEasy Solution\n")

def is_anagramEasy(string1, string2):
    print("Sorted String 1: ", sorted(string1))
    print("Sorted String 2: ", sorted(string2))
    return sorted(string1) == sorted(string2)


print(is_anagramEasy("listens", "silents"))

# 10. ----- * ----- * ----- 3/10 ----- * ----- * ----- Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.
# For example, calling:
# flatten([[1, 2], [3, 4]])
# Should return the list:
# [1, 2, 3, 4]
print("\n10. ----- * ----- * ----- 3/10 ----- * ----- * ----- Flatten a list\n")

def flatten(nestedList):
    flatList = [item for sublist in nestedList for item in sublist]
    return flatList

def flattenLong(nestedList):
    flatList = []
    for sublist in nestedList:
        for item in sublist:
            flatList.append(item)
    return flatList

print("Flatten: ", flatten([[1, 2], [3, 4], [5, 6]]))
print("Flatten nested For-loops: ", flattenLong([[1, 2], [3, 4], [5, 6]]))
flatten = lambda nestedList: [item for sublist in nestedList for item in sublist]
print("Flatten Lambda: ", flatten([[1, 2], [3, 4], [5, 6]]))

# 11. ----- * ----- * ----- 3/10 ----- * ----- * ----- Min-maxing
# Define a function named largest_difference that takes a list of numbers as its only parameter.
# Your function should compute and return the difference between the largest and smallest number in the list.
# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.
# You may assume that no numbers are smaller or larger than -100 and 100.
print("\n11. ----- * ----- * ----- 3/10 ----- * ----- * ----- Min-maxing\n")


def largest_difference(numberedList):
    largest = max(numberedList)
    smallest = min(numberedList)
    return largest - smallest


print(largest_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# short solution
def largest_differenceShort(numbers):
    return max(numbers) - min(numbers)

print(largest_differenceShort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 12. ----- * ----- * ----- 3/10 ----- * ----- * ----- Divisible by 3
# Define a function named div_3 that returns True if its single integer parameter is divisible by 3 and False otherwise.
# For example, div_3(6) is True because 6/3 does not leave any remainder. However div_3(5) is False because 5/3 leaves 2
# as a remainder.
print("\n12. ----- * ----- * ----- 3/10 ----- * ----- * ----- Divisible by 3\n")

def div_3(integer):
    return integer %3 == 0

print(div_3(1))
print(div_3(2))
print(div_3(3))
print(div_3(4))
print(div_3(5))
print(div_3(6))

# 13. ----- * ----- * ----- 4/10 ----- * ----- * ----- Tic tac toe input
# Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:
# 1:  X | O | X
#   -----------
# 2:    |   |
#   -----------
# 3:  O |   |
#    A   B  C
# The board is represented as a 2D list:
#
# board = [
#    ["X", "O", "X"],
#    [" ", " ", " "],
#    ["O", " ", " "],
# ]
# Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you
# need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
# Your task is to write a function that can translate from strings of length 2 to a tuple (row, column).
# Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an
# uppercase letter and a digit.
# For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2
# and column at index 0in the board.
print("\n13. ----- * ----- * ----- 4/10 ----- * ----- * ----- Tic tac toe input\n")


def get_row_col(string):
    row = col = 0

    print("String 0: ", string[0])
    if string[0] == "A":
        col = 0
    elif string[0] == "B":
        col = 1
    elif string[0] == "C":
        col = 2

    print("String 1: ", string[1])
    if string[1] == "1":
        row = 0
    elif string[1] == "2":
        row = 1
    elif string[1] == "3":
        row = 2

    return row, col


print(get_row_col("A3"))
"""
# Short version
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)
"""

# 14. ----- * ----- * ----- 4/10 ----- * ----- * ----- Palindrome
# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd"
# != "dcba".
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the
# string is a palindrome, and False otherwise.
print("\n14. ----- * ----- * ----- 4/10 ----- * ----- * ----- Palindrome\n")

def palindrome(string1):
    return string1 == string1[::-1]

print(palindrome("foofoof"))

# 15. ----- * ----- * ----- 4/10 ----- * ----- * ----- Up and down
# Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing
# two numbers; the first should be one lower than the parameter, and the second should be one higher.
# For example, calling up_down(5) should return (4, 6).
print("\n15. ----- * ----- * ----- 4/10 ----- * ----- * ----- Up and down\n")

def up_down(integer):
    return integer - 1, integer + 1

print(up_down(5))

# 16. ----- * ----- * ----- 4/10 ----- * ----- * ----- Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the
# biggest number of consecutive zeros in the string. For example, given the string: "1001101000110"
# The biggest number of consecutive zeros is 3.
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
# Your function should return the number described above.
print("\n16. ----- * ----- * ----- 4/10 ----- * ----- * ----- Consecutive zeros\n")


def consecutive_zeros(string):
    counter = counterCompare = 0
    binaryList = [item for sublist in string for item in sublist]
    for binary in binaryList:
        if binary == '0':
            counter += 1
            if counter >= counterCompare:
                counterCompare = counter
        elif binary == '1':
                counter = 0

    return counterCompare

print(consecutive_zeros("10000100000111000000"))

# shorter solution
def consecutive_zerosShort(bin_str):
    return max([len(s) for s in bin_str.split("1")])

print(consecutive_zerosShort("10000100000111000000"))

# 17. ----- * ----- * ----- 4/10 ----- * ----- * ----- All equal
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
# For example, calling all_equal([1, 1, 1]) should return True.
print("\n17. ----- * ----- * ----- 4/10 ----- * ----- * ----- All equal\n")


def all_equal(string):
    for character in range(len(string)):
        if string[character] != string[character - 1]:
            return False
    return True

print(all_equal([1, 1, 0, 1, 1]))

# one-liner with nested list comprehension
# and the all() built-in
def all_equalListComprehension(items):
    return all(item1 == item2 for item1 in items for item2 in items)

print(all_equalListComprehension([1, 1, 0, 1, 1]))

# 18. ----- * ----- * ----- 4/10 ----- * ----- * ----- Boolean and
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False
# otherwise.
print("\n18. ----- * ----- * ----- 4/10 ----- * ----- * ----- Boolean and\n")


def triple_and(a, b, c):
    return a and b and c


print(triple_and("a", "b", "c"))

# 19. ----- * ----- * ----- 5/10 ----- * ----- * ----- Writing short code
# Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number
# converted to a string.
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
# What makes this tricky is that your function body must only contain a single line of code.
print("\n19. ----- * ----- * ----- 5/10 ----- * ----- * ----- Writing short code\n")

def convert(numberedList):
    return [str(number) for number in numberedList]


print(convert([1, 2, 3, 4, 5]))

# 20. ----- * ----- * ----- 5/10 ----- * ----- * ----- Custom zip
# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.
# If you don't get it, think of a zipper.
# For example:
#
# zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# )
# Should return:
#
# [(0, 5),
#  (1, 6),
#  (2, 7),
#  (3, 8)]

# Hint
# You can perform a series of checks like this:
#
# if "def" not in code:
#     return "missing def"
# If you get to the last check, we'll try running your code on your code. If this returns "missing param" it's probably
# because you have () in your code somewhere, perhaps in a line such as this:
#
# if "()" in code:
#     return "missing param"
# To get past this, find some clever workaround to still check for "()" without using the literal string.
print("\n20. ----- * ----- * ----- 5/10 ----- * ----- * ----- Custom zip\n")


def zap(aZap, bZap):
    zapList = []
    for count, a in enumerate(aZap):
        zapTuple = (aZap[count], bZap[count])
        zapList.append(zapTuple)
    return zapList


print(zap([0, 1, 2, 3], [5, 6, 7, 8]))

# concise solution with list comprehensions
def zapListComprehension(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

print(zapListComprehension([0, 1, 2, 3], [5, 6, 7, 8]))

# 21. ...?!

# 22. ----- * ----- * ----- 5/10 ----- * ----- * ----- List xor
# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
# Your function must return whether n is exclusively in list1 or list2.
# In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.
#
# For example:
#
# list_xor(1, [1, 2, 3], [4, 5, 6]) == True
# list_xor(1, [0, 2, 3], [1, 5, 6]) == True
# list_xor(1, [1, 2, 3], [1, 5, 6]) == False
# list_xor(1, [0, 0, 0], [4, 5, 6]) == False
print("\n22. ----- * ----- * ----- 5/10 ----- * ----- * ----- List xor\n")


def list_xor(n, list1, list2):
    if n in list1 and n not in list2 or n in list2 and n not in list1:
        return True
    else:
        return False


print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))

# smart solution: uses the built-in xor operator ^
def list_xorOperator(n, list1, list2):
    return (n in list1) ^ (n in list2)

print(list_xorOperator(1, [1, 2, 3], [4, 5, 6]))
print(list_xorOperator(1, [0, 2, 3], [1, 5, 6]))
print(list_xorOperator(1, [1, 2, 3], [1, 5, 6]))
print(list_xorOperator(1, [0, 0, 0], [4, 5, 6]))

# 23. ----- * ----- * ----- 5/10 ----- * ----- * ----- Counting parameters
# Define a function param_count that takes a variable number of parameters. The function should return the number of
# arguments it was called with.
# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
print("\n23. ----- * ----- * ----- 5/10 ----- * ----- * ----- Counting parameters\n")


def param_count(*args):
    return len(args)


print(param_count(1, 2, 3))

# 24. ----- * ----- * ----- 5/10 ----- * ----- * ----- Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.
# Your function should convert the number to a string and add commas as a thousands separator.
# For example, calling format_number(1000000) should return "1,000,000".
print("\n24. ----- * ----- * ----- 5/10 ----- * ----- * ----- Thousands separator\n")


def format_number(number):
    numberString = str(number)
    reverseNumberString = ""
    numCommas = (len(numberString) // 3)
    if len(numberString)%3 == 0:
        numCommas -= 1
    for count, character in enumerate(numberString[::-1]):
        print(count+1, numCommas)
        if ((count+1) % 3 == 0 and numCommas > 0):
            numCommas -= 1
            reverseNumberString += character
            reverseNumberString += ","
        else:
            reverseNumberString += character

    reverseNumberString = reverseNumberString[::-1]
    return reverseNumberString


print(format_number(100))
print(format_number(1000))
print(format_number(10000))
print(format_number(100000))
print(format_number(1000000))
print(format_number(10000000))
print(format_number(100000000))

# built-in solution
def format_numberBest(n):
    #return "{:,}".format(n)
    return f"{n:,}"

print(format_numberBest(100))
print(format_numberBest(1000))
print(format_numberBest(10000))
print(format_numberBest(100000))
print(format_numberBest(1000000))
print(format_numberBest(10000000))
print(format_numberBest(100000000))
result = format_numberBest(1000)
print(result, type(result))


def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."

    # your code here
    for s in string:
        if s not in valid:
            return True
    return False

# PP Final Email Project for the Beginner's Course (good to have, even though it requires improvement).
def is_valid(email):
    if email.count("@") == 1:
        prefix, domain = email.split("@")
        if len(prefix) == 0:
            return False

        if domain.count(".") != 1:
            return False

        domain_name, extension = domain.split(".")
        if len(domain_name) == 0 or len(extension) == 0:
            return False

        if has_invalid_characters(prefix) or has_invalid_characters(domain):
            return False

        return True
    else:
        return False


emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]

for email in emails:
    if is_valid(email):
        print(email + " is valid")
    else:
        print(email + " is invalid")