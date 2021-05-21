temperatureInput = input("Please enter the temperature as a number,followed by either a 'C' for Celsius or\
 'F' for Fahrenheit: ").upper().replace(" ", "")
"""
Enter temperature in either Celsius followed by a 'C' or Fahrenheit followed by an 'F'.

The variable 'temperatureInput' contains the entered temperature and either 'C' or 'F' in uppercase (upper()), and
all the space removed (replace(" ", ""), strip() works equally well here, and will remove all whitespace too).

The 'try-except' statement catches multiple entries of 'C' or 'F' or other characters. The 'if' statement checks
whether the last character in 'temperatureInput' is either a 'C' or an 'F' as well as is the input is not empty,
and executes the relevant statements to convert the entered temperature to Fahrenheit or Celsius, printing the result.
"""

try:
    if temperatureInput != "" and temperatureInput[-1] == "C":
        temperatureInputFloat = float(temperatureInput[:-1])
        fahrenheit = (temperatureInputFloat * 9) / 5 + 32
        print(f"Celsius temperature, {temperatureInputFloat}, is {fahrenheit} in Fahrenheit.")
    elif temperatureInput != "" and temperatureInput[-1] == "F":
        temperatureInputFloat = float(temperatureInput[:-1])
        celsius = (temperatureInputFloat - 32) * 5 / 9
        print(f"Fahrenheit temperature, {temperatureInputFloat}, is {celsius} in Celsius.")
    else:
        print("Please enter a 'C' for Celsius or 'F' for Fahrenheit after the temperature!")
except ValueError:
    print("Please enter a 'C' for Celsius or 'F' for Fahrenheit after the temperature!")
