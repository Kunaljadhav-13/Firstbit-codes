# F
n = 5

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if j == i or j == n:
            print(j, end=" ")
        else:
            print("  ", end=" ")
    print()