# power series

def power_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i ** i

    return sum

n = int(input("Enter n: "))

result = power_series(n)

print("Sum =", result)