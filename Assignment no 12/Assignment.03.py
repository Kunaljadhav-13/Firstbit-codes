# Program to Detect if Two Strings are Anagrams
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
