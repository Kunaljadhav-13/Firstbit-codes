# program to remove all occurrences of a given element in the list
numbers = [10, 20, 10, 30, 40, 10, 50]

num = int(input("Enter element to remove: "))

new_list = []

for element in numbers:
    if element != num:
        new_list.append(element)

print("Original list:", numbers)
print("List after removing:", new_list)
