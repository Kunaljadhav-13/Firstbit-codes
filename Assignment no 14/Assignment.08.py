# Python program to find all the anagrams and group them together from a given list of strings

# Given list of strings
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

# Group anagrams
for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

# Display the groups
print("Anagram groups:")

for group in groups.values():
    print(group)
