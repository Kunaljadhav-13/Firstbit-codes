# Program to find the second largest number using Bubble Sort

numbers = [10, 25, 8, 45, 32, 15]

# Bubble Sort
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Second largest element
second_largest = numbers[-2]

print("Sorted list:", numbers)
print("Second largest number:", second_largest)
