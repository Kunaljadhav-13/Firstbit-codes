# program to reverse three- digit number

# Take a three-digit number from the user
num = int(input("Enter a three-digit number: "))

# Find the digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Reverse the number
reverse = units * 100 + tens * 10 + hundreds

# Display the reversed number
print("Reverse of the number =", reverse)
