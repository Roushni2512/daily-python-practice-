#count vowels and consonants
string = input("Enter a string: ")

vowels = 0
consonants = 0

for char in string:
    if char.isalpha():   # check only alphabets
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
