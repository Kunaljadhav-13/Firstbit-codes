# Recursive function to find sum of n numbers
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)


# Main program
n = int(input("Enter n: "))

result = sum_n(n)

print("Sum =", result)
