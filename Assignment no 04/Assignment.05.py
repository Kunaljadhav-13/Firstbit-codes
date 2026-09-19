# WAP to print fibonncci series upto n

n = int(input('Enter nuber: '))
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c)

    a = b
    b = c