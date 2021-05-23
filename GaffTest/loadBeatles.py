# Created for a friend, to test file handling and line-reading features.

# Using 'with' instead (automatically closes the file).
with open("names.txt", "r") as readBeatles:                         # Open 'names.txt', containing the Beatles names.
    for textLine in readBeatles:                                    # For every line of text...
        firstName, lastName = textLine.split()                      # Split the names into first, and last name.
        print(f"First name: {firstName}, Last name: {lastName}")    # Print first and last name.
        print(textLine)                                             # Print textLine to show it is unchanged.
