fName = input("Please enter your name: ")
age = int(input("Please enter your age in numbers: "))
print(f"Your name is: {fName}")
print(f"Your age is: {age}")

"""
DOCString and/or long code comment to provide insight into how this function works.
"""
# Short comment..

# PEMDAS Rule applies -> parenthesis, exponents, multiplication, division, addition, subtraction
oneNumber = 15
anotherNumber = 6

additionResult = oneNumber + anotherNumber          # 15 + 6 = 21
subtractionResult = oneNumber - anotherNumber       # 15 - 6 = 9
multiplicationResult = oneNumber * anotherNumber    # 15 * 6 = 90
divisionResult = oneNumber / anotherNumber          # 15 / 6 = 2.5
floorDivisionResult = oneNumber // anotherNumber    # 15 // 6 = 2 -> 6 goes into 15 two times (6 * 2 = 12)
moduloResult = oneNumber % anotherNumber            # 15 % 6 = 3 -> 6 goes into 15 twice and the remainder is 3
powerResult = oneNumber ** anotherNumber            # 15 to the power of 6 = 11390625

print(f"additionResult: {additionResult}, subtractionResult: {subtractionResult}")
print(f"multiplicationResult: {multiplicationResult}, powerResult: {powerResult}")
print(f"divisionResult: {divisionResult}, floorDivisionResult: {floorDivisionResult}, moduloResult: {moduloResult}")

stringNameType = "Naoise Olof Seán Gaffney"
intAgeType = 51
floatWeightType = 125.8

print(f"Name, {stringNameType}, is type: ", type(stringNameType))
print(f"Age, {intAgeType}, is type: ", type(intAgeType))
print(f"Name, {floatWeightType}, is type: ", type(floatWeightType))

intString = "3"
print(intString, type(intString))
intString = int(intString)
print(intString, type(intString))