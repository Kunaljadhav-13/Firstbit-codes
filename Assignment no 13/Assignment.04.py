# To Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)
n = int(input("Enter the value of n: "))

dictionary = {}

for x in range(1, n + 1):
    dictionary[x] = x * x

print("Generated dictionary:", dictionary)
