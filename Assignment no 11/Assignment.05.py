# Program to sort a list according to the length of elements within the list

my_list = ["apple", "cat", "banana", "dog", "elephant"]

# Sort the list according to the length of elements
my_list.sort(key=len)

print("Sorted list:", my_list)
