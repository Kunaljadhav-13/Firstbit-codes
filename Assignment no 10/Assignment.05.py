# program to check whether an element is present in a list or not and count how many times list occurs

numbers = [10, 20, 10, 30, 40, 10, 50]

num = int(input("Enter a number: "))

count = 0

for element in numbers:
    if element == num:
        count = count + 1

if count > 0:
    print("Element is present in the list.")
    print("It is present", count, "times.")
else:
    print("Element is not present in the list.")
