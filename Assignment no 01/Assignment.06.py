# Program to find the third angle of a triangle

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))

angle3 = 180 - (angle1 + angle2)

print("Third angle =", angle3)
