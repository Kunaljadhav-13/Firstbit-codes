# Program to remove even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

print("List after removing even numbers:", numbers)
