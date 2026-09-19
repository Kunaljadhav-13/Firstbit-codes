##  Write a program to check whether the triangle is equilateral, isosceles or scalene triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if triangle is valid
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")