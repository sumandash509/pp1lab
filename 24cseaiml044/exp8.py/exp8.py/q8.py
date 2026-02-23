def largest(a,b,c):
    if (a>b and a>c):
        print(f"Largest is a :{a}")
    elif (b>a and b>c):
        print(f"largest is b :{b}")
    elif (c>a and c>b):
        print(f"Largest is c :{c}")
    else :
        print("Either two or three from these numbers are equal...")

a = int(input("Enter a: "))
b = int(input("Enter b :"))
c = int(input("Enter c:"))

largest(a,b,c)