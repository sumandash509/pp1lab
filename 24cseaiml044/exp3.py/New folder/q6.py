ch = input("Enter a character: ").lower()

if 'a' <= ch <= 'z':
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
