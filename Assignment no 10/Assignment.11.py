# Write a program to print all numbers which are divisible by m and n in the
# list
numbers = [10, 15, 20, 30, 40, 45, 60, 75]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Numbers divisible by both", m, "and", n, ":")

for num in numbers:
    if num % m == 0 and num % n == 0:
        print(num)
