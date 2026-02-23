numbers = []
n = int(input("How many numbers do you want to enter? "))
print("Enter the numbers:")
for i in range(n):
    num = int(input())
    numbers.append(num)
unique_sorted = sorted(set(numbers))
print("After removing duplicates and sorting:")
print(unique_sorted)
