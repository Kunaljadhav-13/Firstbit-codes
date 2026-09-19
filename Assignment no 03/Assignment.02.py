#WAP to input any alphabet ans check whether if is vowel or constant
 
character = input("Enter an alphabet: ")

if character in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("Vowel")
else:
    print("Consonant")