# Convert distant given in the feet and inches into meter 
# and cantimeter

feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches
total_cm = total_inches * 2.54

meters = int(total_cm // 100)
centimeters = total_cm % 100

print("Distance:", meters, "meters", centimeters, "centimeters")
