# Write a Python program to find all the unique combinations of 3 numbers from a given
# list of numbers, adding up to a target number

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7]
target = 12

# Set to store unique combinations
combinations = set()

# Find combinations of 3 numbers
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combinations.add(
                    (numbers[i], numbers[j], numbers[k])
                )

# Display the combinations
print("Unique combinations:")

for combination in combinations:
    print(combination)
