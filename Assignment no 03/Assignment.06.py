## Write a program to calculate profit or loss

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
else:
    print("No Profit, No Loss")