from functools import reduce 
no=[1,2,3,4]
total=reduce(lambda x,y:x+y,no)
print("sum:",total)
