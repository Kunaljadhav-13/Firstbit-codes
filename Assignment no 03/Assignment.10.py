## Write a program to check if a person is eligible to marry or not


gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
    print("Eligible for Marriage")
else:
    print("Not Eligible for Marriage")