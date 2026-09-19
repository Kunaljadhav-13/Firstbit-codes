# Python Program to find larger string without using built-in functions

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
    print("Both strings are equal in length")
