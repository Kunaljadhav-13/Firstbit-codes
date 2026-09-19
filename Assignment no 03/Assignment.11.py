# To Calculate total amount of ticket to travel

total = 0

for i in range(1, 6):
    age = int(input("Enter age of person " + str(i) + ": "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        ticket = ticket - (ticket * 0.30)   # 30% discount
    elif age > 59:
        ticket = ticket - (ticket * 0.50)   # 50% discount

    total = total + ticket

print("Total Ticket Amount =", total)