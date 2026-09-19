# Write a program to calculate area of rectangle

def area_rectangle(length, breadth):
    area = length * breadth
    return area

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

result = area_rectangle(l, b)

print("Area of rectangle:", result)