# Recursive function to find sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)


# Main program
n = int(input("Enter a number: "))

result = sum_digits(n)

print("Sum of digits =", result)
