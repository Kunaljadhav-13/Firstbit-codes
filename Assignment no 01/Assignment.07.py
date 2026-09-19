##program to find roots of a quadratic equations

import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b**2-4*a*c

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print("First root =",root1)
print("Second root =",root2)