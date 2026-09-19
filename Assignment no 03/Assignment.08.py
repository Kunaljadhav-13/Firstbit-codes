## Write a program to prompt user to enter userid and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same. 
# If user enters the same number then show him success message otherwise failed

import random

correct_userid = "admin"
correct_password = "1234"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    num = random.randint(1000, 9999)
    print("Random Number:", num)

    user_num = int(input("Enter the same number: "))

    if user_num == num:
        print("Login Successful")
    else:
        print("Verification Failed")
else:
    print("Invalid User ID or Password")