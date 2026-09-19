# To Calculate the Number of Words and the Number of Characters Present in a String
string = input("Enter a string: ")

words = string.split()
word_count = len(words)

character_count = 0

for character in string:
    if character != " ":
        character_count += 1

print("Number of words:", word_count)
print("Number of characters:", character_count)
