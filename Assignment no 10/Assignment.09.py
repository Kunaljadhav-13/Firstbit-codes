n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original list:", numbers)
print("Even elements:", even_list)
print("Odd elements:", odd_list)
