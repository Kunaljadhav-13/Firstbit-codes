# to find sum of three digit number

# Take a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Find the hundreds digit
hundreds = num // 100

# Find the tens digit
tens = (num // 10) % 10

# Find the units digit
units = num % 10

# Calculate the sum of the digits
sum_digits = hundreds + tens + units

# Display the result
print("Sum of digits =", sum_digits)
