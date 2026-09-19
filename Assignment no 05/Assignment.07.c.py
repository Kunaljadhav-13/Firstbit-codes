# Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number of terms: "))

term = 1
s = 0

for i in range(n):
    s = s + term
    term = term * 2

print("Sum =", s)
