# program to print list after removing even numbers
numbers = [10, 15, 20, 25, 30, 35, 40, 45]

new_list = []

for num in numbers:
    if num % 2 != 0:
        new_list.append(num)

print("Original list:", numbers)
print("List after removing even numbers:", new_list)
