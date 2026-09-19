# To Remove the Given Key from a Dictionary
dictionary = {
    "name": "John",
    "age": 20,
    "city": "Pune"
}

key = input("Enter the key to remove: ")

if key in dictionary:
    del dictionary[key]
    print("Updated dictionary:", dictionary)
else:
    print("Key not found in the dictionary")
