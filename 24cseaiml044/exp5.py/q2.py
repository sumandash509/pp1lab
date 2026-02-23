
print("Loop over list:")
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
print("-----")

print("Loop over tuple:")
my_tuple = ("apple", "banana", "cherry")
for fruit in my_tuple:
    print(fruit)
print("-----")

print("Loop over dictionary keys:")
my_dict = {"a": 10, "b": 20, "c": 30}
for key in my_dict:
    print(key, "->", my_dict[key])
print("-----")

print("Loop over set:")
my_set = {"red", "green", "blue"}
for color in my_set:
    print(color)
