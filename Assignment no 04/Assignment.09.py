# WAP to print all numbers in range divisible by a given number 

start = int(input('Enter the starting number: ')) 
end   = int(input('Enter the  ending number: ')) 
d     = int(input('Enter the divisor: '))

print("number divisible by ", d, "are:")

for i in range(start, end + 1):
    if i % d == 0:
        print(i)