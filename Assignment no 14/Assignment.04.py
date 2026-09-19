# Python program that finds all pairs of elements in a list whose sum is equal to a given value

# Given list and target sum
numbers = [2, 4, 3, 5, 7, 8, 9]
target = 10

print("Pairs whose sum is", target, ":")

# Find all pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
