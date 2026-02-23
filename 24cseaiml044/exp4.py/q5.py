
def is_palindrome(num):
    s = str(num)            
    return s == s[::-1]     
n = input("Enter a number: ")

if n.isdigit():
    if is_palindrome(n):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
else:
    print("Please enter a valid number.")
