# To Check if a Given Key Exists in a Dictionary or Not

dictionary = {
    "name": "John",
    "age": 20,
    "city": "Pune"
}

key = input("Enter the key to search: ")

if key in dictionary:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
