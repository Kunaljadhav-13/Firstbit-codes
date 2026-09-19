# program to swap two numbers using third variable

# Take two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap using a third variable
temp = a
a = b
b = temp

# Display the swapped numbers
print("After swapping:")
print("First number =", a)
print("Second number =", b)
