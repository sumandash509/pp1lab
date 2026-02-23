
n = int(input("Enter number of terms: "))  

a = 0
b = 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci series up to", n, "terms:")
    while count < n:
        print(a, end=" ")
        nxt = a + b
        a = b
        b = nxt
        count += 1
