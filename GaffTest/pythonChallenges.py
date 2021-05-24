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


"""
def is_palindrome(string1, string2):
    if string1 == string2[::-1]:
        return True
    else:
        return False

print(is_palindrome("fool", "loof"))
"""