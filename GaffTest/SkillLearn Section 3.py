# Check if the file exists. Requires 'os'.
# Writing/Creating a File, and adding text via the console to it.
import os
if os.path.isfile("TextFile.txt"):
    appendOrDelete = input("Do you want to append 'A' to this file, or delete 'D' it? ").upper().strip()
    if appendOrDelete == "A":
        writeTextFile = open("TextFile.txt", "a", encoding="utf-8")
    elif appendOrDelete == "D":
        os.remove("TextFile.txt")
        writeTextFile = open("TextFile.txt", "w", encoding="utf-8")
else:
    writeTextFile = open("TextFile.txt", "w", encoding="utf-8")

textContent = "\nNaoise Olof Seán Gaffney\n51 years young\n087-9774499"
textContent = textContent + "\n" + input("Do you want to add text to the text file? ")
writeTextFile.write(textContent)
writeTextFile.close()

# Opening/Reading a File.
print("Open File.\n")
openTextFile = open("TextFile.txt", "r", encoding="utf-8")
textFileContent = openTextFile.read()
print("File Content:\n", textFileContent)

# pythonFileContentLine = pythonFile.readline()
# print("Single Line: ", pythonFileContentLine)

# Closing a File.
print("\nClose File.")
openTextFile.close()


# Using 'with' instead (automatically closes the file).
with open("WhileTextFile.txt", "w", encoding="utf-8") as withWriteFile:
    withWriteFile.write(input("Please enter text to add to the file: "))
