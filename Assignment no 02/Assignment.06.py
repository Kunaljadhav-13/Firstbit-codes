# To calculate total salary of employee based on , DA = 10%
# of basic , TA = 12% of basic HRA = 15% of basic

# Take basic salary from the user
basic = float(input("Enter basic salary: "))

# Calculate DA (10% of basic salary)
da = 10 / 100 * basic

# Calculate TA (12% of basic salary)
ta = 12 / 100 * basic

# Calculate HRA (15% of basic salary)
hra = 15 / 100 * basic

# Calculate total salary
total_salary = basic + da + ta + hra

# Display the total salary
print("Total Salary =", total_salary)

