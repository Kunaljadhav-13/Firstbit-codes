# Program to create lists of numbers, squares and cubes

numbers = []
squares = []
cubes = []

for i in range(1, 11):
    numbers.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
