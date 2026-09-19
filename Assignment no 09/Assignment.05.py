# program to find factorial using recursion
# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Main program
n = int(input("Enter a number: "))

result = factorial(n)

print("Factorial =", result)
