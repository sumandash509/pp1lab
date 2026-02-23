celsius_list = [0, 20, 30, 37, 100]

fahrenheit_list = []

for c in celsius_list:
    f = (c * 9/5) + 32
    fahrenheit_list.append(f)

print("Celsius -> Fahrenheit")
for i in range(len(celsius_list)):
    print(celsius_list[i], "°C ->", fahrenheit_list[i], "°F")
