# Write a program to check if entered number is a palindrome or not

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome number")
else:
    print("Not a palindrome number")