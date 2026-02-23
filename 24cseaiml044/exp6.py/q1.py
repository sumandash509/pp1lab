fruits = ["apple", "banana", "mango","grapes" ,"orange"]
print(" fruits in reverse order:")
for fruit in reversed (fruits):
    print(fruits)
print("\nLength of each fruit name:")
for fruits in fruits:
    print(fruits, ":", len(fruits))
rev_fruits = []
for fruits in fruits:
    rev_fruits.append(fruits[::-1])
print("\nlist of reversed fruits names :")
print(rev_fruits)
