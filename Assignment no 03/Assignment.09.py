## Input 5 subject marks from user and display grade(eg.First class, Second class ..) 

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

print("Percentage =", per)

if per >= 75:
    print("Distinction")
elif per >= 60:
    print("First Class")
elif per >= 50:
    print("Second Class")
elif per >= 35:
    print("Pass")
else:
    print("Fail")