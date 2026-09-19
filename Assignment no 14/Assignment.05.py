# Write a Python program to find the longest common prefix of all strings,  Use the Python set.

# List of strings
strings = ["flower", "flow", "flight"]

# Find the shortest string
shortest = min(strings, key=len)

# Find the longest common prefix
prefix = ""

for i in range(len(shortest)):
    # Use set to check characters at the same position
    chars = {s[i] for s in strings}

    if len(chars) == 1:
        prefix += shortest[i]
    else:
        break

print("Longest Common Prefix:", prefix)
