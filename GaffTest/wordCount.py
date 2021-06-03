# Revised version of the 'words.py' found in the 'Code3' directory.
# Request the filename to perform the word count on. Remove whitespaces, '.strip()'.
name = input('Enter file: ').strip()

try:
    with open(name, 'r', encoding="utf-8") as handle:
        # Count word frequency, line-by-line from the file. Split the words to count them.
        # Use '.get()' to perform the counting.
        counts = {}
        for line in handle:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1

        # Find the most common word, 'bigword', and the number of times it occurs 'bigcount'.
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
sortedWordCountDict = dict(sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
print(sortedWordCountDict)
