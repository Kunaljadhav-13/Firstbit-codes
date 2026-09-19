# Recursive function to find Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Main program
n = int(input("Enter number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")
