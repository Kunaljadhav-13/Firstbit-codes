# program to swap two numbers without using third variable

# Take two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap the numbers
a, b = b, a

# Display the swapped numbers
print("After swapping:")
print("First number =", a)
print("Second number =", b)
