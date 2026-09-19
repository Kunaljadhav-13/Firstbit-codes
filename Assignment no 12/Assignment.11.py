# replace every blank space with hyphen in a string

string = input("Enter a string: ")

result = ""

for char in string:
    if char == " ":
        result += "-"
    else:
        result += char

print("String after replacing spaces with hyphens:", result)
