n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
   
    for j in range(i):
        print(i + j, end=" ")

    # Decreasing numbers
    for j in range(i - 2, -1, -1):
        print(i + j, end=" ")

    print()