while True:
    line = input("Please enter 'stuff': ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("All done!")

for integer in range(5,0,-1):
    print(integer)
print("All done!")