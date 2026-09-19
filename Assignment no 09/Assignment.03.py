# Recursive function to reverse a number
def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse(n // 10, rev)


# Main program
num = int(input("Enter a number: "))

result = reverse(num)

print("Reverse =", result)
