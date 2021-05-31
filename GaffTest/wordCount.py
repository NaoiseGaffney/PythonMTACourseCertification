# Get the name of the file and open it
name = input('Enter file: ').strip()

try:
    with open(name, 'r', encoding="utf-8") as handle:
        # Count word frequency
        counts = {}
        for line in handle:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1

        # Find the most common word
        bigcount = None
        bigword = None
        for word, count in counts.items():
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count
except FileNotFoundError:
    print("Please enter a valid filename.")
    exit(-1)


print(f"Most common 'word' is: '{bigword}', and it occurs {bigcount} time(s).")
tuple_in_right_order = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print(tuple_in_right_order)
