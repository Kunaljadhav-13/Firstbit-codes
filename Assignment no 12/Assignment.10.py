# Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

count1 = 0
count2 = 0

for char in string1:
    count1 += 1

for char in string2:
    count2 += 1

if count1 > count2:
    print("Larger string:", string1)
elif count2 > count1:
    print("Larger string:", string2)
else:
    print("Both strings are of equal length")
