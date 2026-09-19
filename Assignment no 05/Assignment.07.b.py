n = int(input("Enter N: "))

s = 0

for i in range(1, n + 1):
    s = s + n ** i

print("Sum =", s)
