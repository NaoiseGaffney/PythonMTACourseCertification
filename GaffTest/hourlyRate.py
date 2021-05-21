inputHours = 0
inputRate = 0
currencyList = ("€", "£", "$", "¥", "¢")
inputCurrencySymbol = ""

try:
    inputCurrencySymbol = input("Please enter a currency symbol (€, £, $, ¥, ¢), or return for none: ")
    inputHours = input("Please enter your hours: ")
    inputHours = float(inputHours)
    inputRate = input("Please enter your hourly rate: ")
    inputRate = float(inputRate)
except ValueError:
    print("You must enter hours and rates as numbers (integer or float), and not as text (string).")
finally:
    if type(inputHours) and type(inputRate) == float:
        salary = inputHours * inputRate
        if inputCurrencySymbol not in currencyList:
            inputCurrencySymbol = ""
        print(f"Your salary is: {inputCurrencySymbol}{inputHours} * {inputCurrencySymbol}{inputRate} = {inputCurrencySymbol}{salary}")

"""
inputHours = 0
inputRate = 0
salary = 0

def calculateSalary(inputHours, inputRate):
    inputCurrencySymbol = ""
    currencyList = ("€", "£", "$", "¥", "¢")
    if type(inputHours) and type(inputRate) == float:
        salary = inputHours * inputRate
        if inputCurrencySymbol not in currencyList:
            inputCurrencySymbol = ""
    return salary

try:
    inputCurrencySymbol = input("Please enter a currency symbol (€, £, $, ¥, ¢), or return for none: ")
    inputHours = input("Please enter your hours: ")
    inputHours = float(inputHours)
    inputRate = input("Please enter your hourly rate: ")
    inputRate = float(inputRate)
except ValueError:
    print("You must enter hours and rates as numbers (integer or float), and not as text (string).")
finally:
    salary = calculateSalary(inputHours, inputRate)
    print(f"Your salary is: {inputCurrencySymbol}{inputHours} * {inputCurrencySymbol}{inputRate} = {inputCurrencySymbol}{salary}")
"""