# To count number of digits and letters in a string

string = input("Enter a string: ")

letters = 0
digits = 0

for char in string:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letters += 1
    elif char >= '0' and char <= '9':
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)
