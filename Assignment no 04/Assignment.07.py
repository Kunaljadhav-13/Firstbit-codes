# WAP to print all integers upto n that are not divisible by 2 and 3

n = int(input("Enter value of n:"))

print("numbers not divisible by 2 and 3 are:")
for i in range(1, n+1):
    if i % 2 !=0 and i % 3 !=0:
         print(i)