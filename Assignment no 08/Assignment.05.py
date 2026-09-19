# Sum of all prime numbers between 1 to n

def sum_prime(n):
    total = 0

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            total = total + num

    return total

n = int(input("Enter n: "))

result = sum_prime(n)

print("Sum of prime numbers =", result)