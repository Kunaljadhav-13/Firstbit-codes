# Python Program to Multiply All the Items in a Dictionary

dictionary = {
    "a": 2,
    "b": 3,
    "c": 4,
    "d": 5
}

product = 1

for value in dictionary.values():
    product *= value

print("Product of all items:", product)
