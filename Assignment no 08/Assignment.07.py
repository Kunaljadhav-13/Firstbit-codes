# Write a program to find sum of digits of a number

def sum_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total

num = int(input("Enter a number: "))

result = sum_digits(num)

print("Sum of digits =", result)