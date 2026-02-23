n = int(input("Enter a Number:"))

def fact(n,fact):
    for i in range(1,n+1):
        fact = fact*i
    return fact
factorial = fact(n,1)
print("Factorial :",factorial)