
def count(str):
    vow = 0
    vowels = "AEIOUaeiou"
    for s in str:
        if s in vowels:
            vow = vow +1

    return vow


str = input("Enter a string:")

countt = count(str)
print(f"The no of vowels in string are : {countt}")