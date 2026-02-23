a = 0
b = 1

fib_sequence = []

while a <= 1000:
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci series up to 1000:")
print(fib_sequence)

sum_even = 0
for num in fib_sequence:
    if num % 2 == 0:
        sum_even += num

print("Sum of even-valued terms:", sum_even)
