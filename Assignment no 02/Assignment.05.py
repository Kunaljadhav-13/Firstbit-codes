# To calculate selling price of book based on cost price 
# and discount

 # Take the cost price of the book
cost_price = float(input("Enter cost price of the book: "))

# Take the discount percentage
discount = float(input("Enter discount percentage: "))

# Calculate the discount amount
# Formula: Discount Amount = Cost Price × Discount / 100
discount_amount = cost_price * discount / 100

# Calculate the selling price
# Formula: Selling Price = Cost Price - Discount Amount
selling_price = cost_price - discount_amount

# Display the result
print("Selling Price of the book =", selling_price)
