# Given two sets of numbers, write a Python program to find the missing numbers in the second set 
# as compared to the first and vice versa. Use the Python set.

# Given two sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

# Numbers missing in set2 compared to set1
missing_in_set2 = set1 - set2

# Numbers missing in set1 compared to set2
missing_in_set1 = set2 - set1

print("Missing in second set:", missing_in_set2)
print("Missing in first set:", missing_in_set1)
