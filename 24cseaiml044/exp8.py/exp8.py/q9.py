def simIn(p,r,t):
    si = (p*r*t)/100
    return si

p = float(input("Enter Principle:"))
r = float(input("Enter rate:"))
t = float(input("Enter time :"))


si=simIn(p,r,t)

print(f"Simple Intrest:{si}")
