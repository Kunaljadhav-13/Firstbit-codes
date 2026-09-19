numbers = [10, 25, 5, 40, 15]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum element:", maximum)
print("Minimum element:", minimum)
