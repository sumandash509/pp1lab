n = int(input("Enter a no:"))

def primeCheck(n):
    count = 0
    for i in range(1,n):
        if(n%i == 0):
            count = count+1
    return count   
count = primeCheck(n)
if count == 2:
    print("Prime no")
else :
    print("Not a prime no")