# 3

passengers = int (input ("enter number of passengers:"))
tickets = float(input ("enter tickets cost: "))

total_amount = 0

for i in range(1, passengers + 1):

    age = int(input(f"enter age of passengers {i}:"))

    if age < 12:
        amount = tickets (tickets * 30 / 100)
        print("30% Discount =", amount)

    elif age > 59:
        amount = tickets - (tickets * 50 / 100)
        print("50% Discount =",amount)


    else:
        amount = tickets
        print("full tickets =", amount)

    total_amount += amount


print("\ntotal ticket amount =", total_amount)