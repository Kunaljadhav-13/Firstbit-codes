# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

string = input("Enter a string: ")

if len(string) > 1:
    result = string[-1] + string[1:-1] + string[0]
else:
    result = string

print("New string:", result)
