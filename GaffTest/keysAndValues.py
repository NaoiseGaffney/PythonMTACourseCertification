# A simple dictionary
x = {'X':"yes", 'Y':"no", 'Z':"ok"}

# To print a specific key (for example key at index 1)
print([key for key in x.keys()][1])

# To print a specific value (for example value at index 1)
print([value for value in x.values()][1])

# To print a pair of a key with its value (for example pair at index 2)
print(([key for key in x.keys()][2], [value for value in x.values()][2]))

# To print a key and a different value (for example key at index 0 and value at index 1)
print(([key for key in x.keys()][0], [value for value in x.values()][1]))

# To print all keys and values concatenated together
print(''.join(str(key) + '' + str(value) for key, value in x.items()))

# To print all keys and values separated by commas
print(', '.join(str(key) + ', ' + str(value) for key, value in x.items()))

# To print all pairs of (key, value) one at a time
for e in range(len(x)):
    print(([key for key in x.keys()][e], [value for value in x.values()][e]))

# To print all pairs (key, value) in a tuple
print(tuple(([key for key in x.keys()][i], [value for value in x.values()][i]) for i in range(len(x))))