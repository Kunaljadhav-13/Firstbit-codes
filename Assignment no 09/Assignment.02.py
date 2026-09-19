# Recursive function to calculate sum of powers of digits
def armstrong(n, digits):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** digits) + armstrong(n // 10, digits)


# Main program
num = int(input("Enter a number: "))

digits = len(str(num))
result = armstrong(num, digits)

if result == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
