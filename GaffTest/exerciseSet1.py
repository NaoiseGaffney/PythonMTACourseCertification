# Question 1
# Write a program which will find all numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# Consider use range(#begin, #end) method
print("\33[91m\nQuestion 1 - Div by 7, though not Div by 5: \33[0m")
print([number for number in range(2000, 3201) if number % 5 != 0 and number % 7 == 0])

number_string = ""
for number in range(2000, 3201):
    if number % 5 != 0 and number % 7 == 0:
            number_string += str(number) + ", "

number_string = number_string[:-2]
print(type(number_string), number_string)


# Question 2
# Write a program which can compute the factorial of a given number.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# e.g Factorial 8 is calculated as 8x7x6x5x4x3x2x1
# In case of input data being supplied to the question, it should be assumed to be a console
# input.
# Two ways...for-lopp with range()...
print("\33[91m\nQuestion 2 - Factorial: \33[0m")
factorial = 1
factorial_list = {}
number = abs(int(input("Please enter a whole number (integer): ").strip()))
for i in range(1, number + 1):
    factorial = factorial * i
    factorial_list[i] = factorial
print(f"Factorial of {number} is {factorial}.")
print(factorial_list)

# List Comprehension
print([factorial * i for i in range(1, 2)])


# Question 3
# Write and test a function which takes one argument (a year) and returns True if the year is a leap
# year, or False otherwise. The seed of the function is already sown in the skeleton code (below).
# Note: we’ve also prepared a short testing code, which you can use to test your function. The
# code uses two lists – one with the test data, and the other containing the expected results.
# The code will tell you if any of your results are invalid.
print("\33[91m\nQuestion 3 - Leap Year: \33[0m")


def IsYearLeap(year):
    """
    Checks whether a year is a Leap Year. Centuries that are divisible by 400 but not 100 are Leap Years. Otherwise
    all other years that are divisible by 4 are Leap Years.
    Rules: Leap years occur on years where the second two digits (AD only) are divisible by 4. In the event of the last
    two digits being 00, the first two digits must also be divisible by 4 for the year to be a leap year. For BC,
    counting starts at 1, so there is no year 0. This means that the leap years are offset by 1 and can be calculated
    by the same method as above, but with the year number increased by 1: https://www.howtocreate.co.uk/php/leapyear.php
    :param year: year is an integer (negative or positive)
    :return: True if a Leap Year, or False if not.
    """
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    else:
        return False


# Test Data and Results expanded to perform extended tests.
testdata = [1900, 2000, 2016, 1987, 100, 2020, 2021, 0, 1896, 1904]
testresults = [False, True, True, False, False, True, False, True, True, True]
for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "-> ", end="")
    result = IsYearLeap(yr)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")


# Question 4
# Write and test a function which takes two arguments (a year and a month) and returns the
# number of days for the given month/year pair (yes, we know that only February is sensitive
# to the year value, but we want our function to be universal). The initial part of the function
# is ready. Now, convince the function to return None if its arguments don’t make sense.
# Of course, you can (to be honest: you should!) use the previously written and tested function. It may
# be very helpful (we cannot say anything more, sorry). We encourage you to use a list filled with the
# months’ lengths. You can create it inside the function – this trick will significantly shorten the code.
# We’ve prepared a testing code. Expand it to include more test cases.
print("\33[91m\nQuestion 4 - Leap Year and Month: \33[0m")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # List of number of days per month, non-Leap Year.


def IsYearLeap(year):
    """
    Checks whether a year is a Leap Year. Centuries that are divisible by 400 but not 100 are Leap Years. Otherwise
    all other years that are divisible by 4 are Leap Years.
    Rules: Leap years occur on years where the second two digits (AD only) are divisible by 4. In the event of the last
    two digits being 00, the first two digits must also be divisible by 4 for the year to be a leap year. For BC,
    counting starts at 1, so there is no year 0. This means that the leap years are offset by 1 and can be calculated
    by the same method as above, but with the year number increased by 1: https://www.howtocreate.co.uk/php/leapyear.php
    :param year: year is an integer (negative or positive)
    :return: True if a Leap Year, or False if not.
    """
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    else:
        return False


def DaysInMonth(year, month):
    """
    Checks number of days per months, including Leap Years (February 29th).
    :param year: year is an integer (negative or positive)
    :param month: month is an integer that is checked against the list 'days_in_month' to calculate days.
    :return: 29 for a Leap Year February, or the number of days in the month.
    """
    if IsYearLeap(year) and month == 2:
        return 29
    else:
        return days_in_month[month - 1]


# Test Years, Months, and Days expanded to perform extended positive and negative tests.
testyears = [1900, 2000, 2016, 1987, 2020, 2020, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021]
testmonths = [2, 2, 1, 11, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
testresults = [28, 29, 31, 30, 28, 29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "-> ", end="")
    result = DaysInMonth(yr, mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")


# Question 5
# Write and test a function which takes three arguments (a year, a month, and a day of the
# month) and returns the corresponding day of the year, or returns None if any of the
# arguments is invalid.
# Use the previously written and tested functions. Add some test cases to the code. Our test is
# only a beginning.
print("\33[91m\nQuestion 5 - Leap Year, Month, and Day: \33[0m")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # List of number of days per month, non-Leap Year.
print(sum(days_in_month))                                           # Validating the list adds up to 365.


def IsYearLeap(year):
    """
    Checks whether a year is a Leap Year. Centuries that are divisible by 400 but not 100 are Leap Years. Otherwise
    all other years that are divisible by 4 are Leap Years.
    Rules: Leap years occur on years where the second two digits (AD only) are divisible by 4. In the event of the last
    two digits being 00, the first two digits must also be divisible by 4 for the year to be a leap year. For BC,
    counting starts at 1, so there is no year 0. This means that the leap years are offset by 1 and can be calculated
    by the same method as above, but with the year number increased by 1: https://www.howtocreate.co.uk/php/leapyear.php
    :param year: year is an integer.
    :return: True if a Leap Year, or False if not.
    """
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    else:
        return False


def DaysInMonth(year, month):
    """
    Checks number of days per months, including Leap Years (February 29th).
    :param year: year is an integer (negative or positive)
    :param month: month is an integer that is checked against the list 'days_in_month' to calculate days.
    :return: 29 for a Leap Year February, or the number of days in the month.
    """
    if IsYearLeap(year) and month == 2:
        return 29
    else:
        return days_in_month[month - 1]


def DayOfYear(year, month, day):
    """
    Validate year, month and day before performing calculations. January is easy, it's the number of days as defined by
    the value in 'day'. February is January (31) + number of days in February as defined by 'day'. Add all days of the
    month up until current month-1, then add one (1) for February if Leap Year. Add number of days in month to
    'total_days' before adding number of days per month before current month.
    :param year: year is an integer (negative or positive).
    :param month: month is an integer that is checked against the list 'days_in_month' to calculate days.
    :param day: day is an integer that is checked against the list 'days_in_month'.
    :return: total_days is an integer containing the total number of days if data is valid, or None if not.
    """
    total_days = 0
    # Validate the date ranges, months (1 to 12), and days (correct number of days per month), including Leap Year.
    if 0 < month <= 12 and (0 < day <= days_in_month[month - 1] or (IsYearLeap(year) and 2 == month <= days_in_month[month - 1] +1)):
        # January is easy, it's the number of days as defined by the value in 'day'.
        if month == 1:
            total_days = day
            return total_days
        # February is January (31) + number of days in February as defined by 'day'.
        if month == 2:
            total_days = day + days_in_month[0]
            return total_days
        # Add all days of the month up until current month-1, then add one (1) for February if Leap Year.
        total_days = day    # Add number of days in month to 'total_days' before adding number of days per month before current month.
        for m in range(month - 1):
            total_days += days_in_month[m]
        if IsYearLeap(year):
            total_days += 1  # Leap Year Day, February 29
        return total_days
    else:
        return None         # Invalid month or day.


# Performing extended positive and negative tests.
print("DayOfYear(1900, 2, 29)", DayOfYear(1900, 2, 29))
print("DayOfYear(1900, 2, 28)", DayOfYear(1900, 2, 28))
print("DayOfYear(2000, 1, 31)", DayOfYear(2000, 1, 31))
print("DayOfYear(2000, 1, 32)", DayOfYear(2000, 1, 32))
print("DayOfYear(2000, 12, 31)", DayOfYear(2000, 12, 31))
print("DayOfYear(2000, 2, 28)", DayOfYear(2000, 2, 28))
print("DayOfYear(2000, 1, 29)", DayOfYear(2000, 1, 29))
print("DayOfYear(2000, 13, 31)", DayOfYear(2000, 13, 31))
print("DayOfYear(2001, 2, 28)", DayOfYear(2001, 2, 28))
print("DayOfYear(2001, 2, 29)", DayOfYear(2001, 2, 29))
print("DayOfYear(2001, 13, 33)", DayOfYear(2001, 13, 33))
print("DayOfYear(2001, 0, 0)", DayOfYear(2001, 0, 0))
print("DayOfYear(2001, 1, 20)", DayOfYear(2001, 1, 20))
print("DayOfYear(2001, 2, 20)", DayOfYear(2001, 2, 20))
print("DayOfYear(2001, 3, 20)", DayOfYear(2001, 3, 20))
print("DayOfYear(2000, 3, 20)", DayOfYear(2000, 3, 20))
print("DayOfYear(0, 3, 20)", DayOfYear(0, 3, 20))
print("DayOfYear(-100, 3, 20)", DayOfYear(-100, 3, 20))
print()
print("\nJanuary")
print("DayOfYear(2000, 1, 31)", DayOfYear(2000, 1, 31))
print("DayOfYear(2003, 1, 31)", DayOfYear(2003, 1, 31))
print("\nFebruary")
print("DayOfYear(2000, 2, 29)", DayOfYear(2000, 2, 29))
print("DayOfYear(2003, 2, 29)", DayOfYear(2003, 2, 29))
print("DayOfYear(2003, 2, 28)", DayOfYear(2003, 2, 28))
print("\nMarch")
print("DayOfYear(2000, 3, 31)", DayOfYear(2000, 3, 31))
print("DayOfYear(2003, 3, 31)", DayOfYear(2003, 3, 31))
print("\nApril")
print("DayOfYear(2000, 4, 30)", DayOfYear(2000, 4, 30))
print("DayOfYear(2003, 4, 30)", DayOfYear(2003, 4, 30))
print("\nMay")
print("DayOfYear(2000, 5, 31)", DayOfYear(2000, 5, 31))
print("DayOfYear(2003, 5, 31)", DayOfYear(2003, 5, 31))
print("\nJune")
print("DayOfYear(2000, 6, 30)", DayOfYear(2000, 6, 30))
print("DayOfYear(2003, 6, 30)", DayOfYear(2003, 6, 30))
print("\nJuly")
print("DayOfYear(2000, 7, 31)", DayOfYear(2000, 7, 31))
print("DayOfYear(2003, 7, 31)", DayOfYear(2003, 7, 31))
print("\nAugust")
print("DayOfYear(2000, 8, 31)", DayOfYear(2000, 8, 31))
print("DayOfYear(2003, 8, 31)", DayOfYear(2003, 8, 31))
print("\nSeptember")
print("DayOfYear(2000, 9, 30)", DayOfYear(2000, 9, 3))
print("DayOfYear(2003, 9, 30)", DayOfYear(2003, 9, 3))
print("\nOctober")
print("DayOfYear(2000, 10, 31)", DayOfYear(2000, 10, 31))
print("DayOfYear(2003, 10, 31)", DayOfYear(2003, 10, 31))
print("\nNovember")
print("DayOfYear(2000, 11, 30)", DayOfYear(2000, 11, 30))
print("DayOfYear(2003, 11, 30)", DayOfYear(2003, 11, 30))
print("\nDecember")
print("DayOfYear(2000, 12, 31)", DayOfYear(2000, 12, 31))
print("DayOfYear(2003, 12, 31)", DayOfYear(2003, 12, 31))


# Question 6
# A natural number is prime if it is greater than 1 and has no divisors other than 1 and
# itself.
# Complicated? Not at all. Look: 8 isn’t a prime number, as you can divide it by 2 and 4
# (we can’t use divisors equal to 1 and 8 as the definition prohibits this). On the other
# hand, 7 is a prime number, as we can’t find any legal divisors for it.
# Write a function checking whether a number is prime or not.
# The function:
# • is called IsPrime;
# • takes one argument (the value to check)
# • returns True if the argument is a prime number, and False otherwise.
# Hint: try to divide the argument by all subsequent values (starting from 2) and check the
# remainder – if it’s zero, your number cannot be a prime; think carefully about when you
# should stop the process.
# If you need to know the square root of any value, you can utilize the ** operator. Remember:
# the square root of x is the same as x ** 0.5 ( x raised to the power of 1.5).
# Complete the code presented below.
# Run your code and check whether your output is the same as ours.
print("\33[91m\nQuestion 6 - Prime Number: \33[0m")

# number = abs(int(input("Please enter a number: ").replace(" ", "")))
def IsPrime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not a prime number")    # Number is divisible by a number not the same as itself
                break
        else:
            print(f"\33[91m{number}\33[0m"
                  f" is a prime number")                    # Number is not divisible by any number from 2 to number-1
    else:
        print(f"{number} is not a prime number")            # Number is 1 or less.


for i in range(200):
    IsPrime(i + 1)
