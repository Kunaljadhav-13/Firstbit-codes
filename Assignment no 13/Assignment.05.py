# Python Program to Sum All the Items in a Dictionary

dictionary = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

total = 0

for value in dictionary.values():
    total += value

print("Sum of all items:", total)
