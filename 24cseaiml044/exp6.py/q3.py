sentence = input("Enter a sentence: ")
LIST1 = sentence.split()
print("\nElements of LIST1 with index:")
for index, word in enumerate(LIST1):
    print(index, word)
LIST2 = list(range(1, len(LIST1) + 1))
LIST3 = list(zip(LIST1, LIST2))
print("\nCombined List (LIST3):")
print(LIST3)
