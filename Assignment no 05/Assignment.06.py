# Write a program to print first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

print("first", n, "prime numbersw are:")

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1

    num += 1
    