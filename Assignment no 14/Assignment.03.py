# Program to find all the unique words and count the frequency of occurrence from a given list of strings.
#  Use Python set data type

# List of strings
strings = [
    "Python is easy",
    "Python is powerful",
    "Learning Python is fun"
]

# Convert all strings into a list of words
words = []
for s in strings:
    words.extend(s.lower().split()) # Convert to lowercase and split into words

# Find unique words using set
unique_words = set(words)

# Count frequency of each unique word
print("Word Frequencies:")
for word in unique_words:
    print(word, ":", words.count(word))
