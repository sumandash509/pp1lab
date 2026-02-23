def reverse_str(str):
    reversed_str = ""
    for i in str:
        reversed_str = i + reversed_str
    print(reversed_str)

str = input("Enter a String to revrse:")

reverse_str(str)