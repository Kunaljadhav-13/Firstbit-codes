# To find the two numbers whose product is maximum among all the pairs in a given list of numbers.
#  Use the Python set

# Given list of numbers
numbers = [2, 5, 3, 8, 6, 1]

# Convert list to set to get unique numbers
num_set = set(numbers)

max_product = None
max_pair = ()

# Find all pairs
num_list = list(num_set)

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        product = num_list[i] * num_list[j]

        if max_product is None or product > max_product:
            max_product = product
            max_pair = (num_list[i], num_list[j])

print("Two numbers:", max_pair)
print("Maximum product:", max_product)
