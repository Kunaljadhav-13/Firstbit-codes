# 
numbers = [10, 20, 30, 40, 50]

reverse_list = []

for i in range(len(numbers) - 1, -1, -1):
    reverse_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reverse_list)
