# Program to separate even and odd elements in two diferent lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even elements:", even)
print("Odd elements:", odd)
