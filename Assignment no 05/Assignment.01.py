# Write a program to prompt user to enter userid and password
#  If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times
# After that program to terminate

userid = "admin"
password = "admin123"

for i in range(1,4):
     uid = input("enter userid:") 
     pwd=input("enter password:")

     if uid == userid and pwd == password:
            print("login successful")
            break 
     else: 
        print("incrorrect user id or password ")
    
        if i == 3: 
            print("program terminated")