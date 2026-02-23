import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

gcd_3 = math.gcd(math.gcd(a, b), c)
print("GCD =", gcd_3)
