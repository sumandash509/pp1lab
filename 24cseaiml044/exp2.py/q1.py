p=int(input("enter the principle amount:"))
r=float(input("enter the rate of  interest:"))
t=int(input("enter the total time:"))
n=int(input("enter the no of compound per year:"))
a=int(input("enter the final amount:"))
si = (p*t*r)/100
print("simple interest is:",si)
a = p*(1+r/100)**t
ci=a-p
print("compound interest is:",ci)