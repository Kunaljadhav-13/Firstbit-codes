# factorial series

def factorial_series(n):
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact

    return sum

n = int(input("Enter n: "))
result = factorial_series(n)
print("Sum =", result)