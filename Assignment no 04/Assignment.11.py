# WAP to check if given number Strong Number

num = int(input('Enter a number:'))

temp = num 
sum = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact + 1

    sum = sum + fact
    temp = fact // 10

    if sum == num:
        print(num, " is a strong number")
    else:
           print(num, " is not a strong number")