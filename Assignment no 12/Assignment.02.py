# to Remove the nth Index Character from a Non-Empty String

string = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

result = string[:n] + string[n+1:]

print("String after removing character:", result)
