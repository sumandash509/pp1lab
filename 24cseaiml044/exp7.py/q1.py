m = int(input("Enter m: "))
n = int(input("Enter n: "))

numbers = []
for i in range(m, n + 1):
    numbers.append(i)

print("List:", numbers)

total = 0
for num in numbers:
    total += num
print("Sum:", total)
