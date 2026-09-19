# Program to sort the list according to the second element

my_list = [[1, 5], [2, 3], [3, 8], [4, 2]]

# Sort according to the second element
my_list.sort(key=lambda x: x[1])

print("Sorted list:", my_list)
