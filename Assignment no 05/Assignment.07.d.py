# S = a + a²/2 + a³/3 + ...... + a¹⁰/10
a = float(input("Enter a: "))

s = 0

for i in range(1, 11):
    s = s + (a ** i) / i

print("Sum =", s)
