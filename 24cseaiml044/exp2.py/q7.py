
i = int(input("Enter an integer: "))
s = input("Enter a string: ")
f = float(input("Enter a float number: "))
b = input("Enter True/False: ")   # boolean comes as string first
b = b == "True"                   # convert to boolean
c = complex(input("Enter a complex number (e.g., 3+4j): "))

print("Type of integer:", type(i))
print("Type of string:", type(s))
print("Type of float:", type(f))
print("Type of boolean:", type(b))
print("Type of complex:", type(c))
