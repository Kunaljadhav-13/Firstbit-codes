# WAP to check if given number is Perfect Number

num = int(input('Enter a number:'))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + 1

if sum == num:
    print(num, " is a perfect number ")
else:
    print(num, " is a not  perfect number ")