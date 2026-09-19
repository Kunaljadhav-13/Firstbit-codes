# WAP to print Armstrong number within a given range

start = int(input("Enter a starting number:"))
end = int(input("Enter a ending number:"))

print("armstorng numbers are:")

for num in range(start, end+ 1):
    temp = num
    digit = len(str(num))
    sum = 0 

    while temp > 0:
         digit = temp % 10
         sum = sum + digit ** digit
         temp = temp // 10

         if sum == num:
           print(num)
