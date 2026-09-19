# Program to convert days into years, weeks and days

days = int(input("Enter number of days: "))

# Calculate years
years = days // 365

# Calculate remaining days after years
remaining_days = days % 365

# Calculate weeks
weeks = remaining_days // 7

# Calculate remaining days
remaining_days = remaining_days % 7

# Display the result
print("Years =", years)
print("Weeks =", weeks)
print("Days =", remaining_days)
