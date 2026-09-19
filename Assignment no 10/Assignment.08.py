# program to create a duplicate of an existing list. It should not point to
#same list
numbers = [10, 20, 30, 40, 50]

duplicate = []

for num in numbers:
    duplicate.append(num)

print("Original list:", numbers)
print("Duplicate list:", duplicate)

# Changing duplicate list
duplicate[0] = 100

print("After changing duplicate:")
print("Original list:", numbers)
print("Duplicate list:", duplicate)
