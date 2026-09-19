# Print 1 to 100 in Snakes and Ladders pattern

num = 1

for row in range(10):
    numbers = list(range(num, num + 10))

    if row % 2 == 1:
        numbers.reverse()

    print(*numbers)
    num += 10
