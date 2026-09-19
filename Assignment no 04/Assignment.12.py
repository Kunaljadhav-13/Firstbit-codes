# Write a program to check if given number is Armstrong number or not

num = int(input("enter a number:"))

temp = num
count = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == num:
    print(num, " is an armstrong number")

else:
    print(num, " is not an armstrong")