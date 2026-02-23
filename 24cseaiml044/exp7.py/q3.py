text = "python is easy"
words = text.split()
print("Number of words:", len(words))
palindrome = 0
for w in words:
    if w == w[::-1]:
        palindrome += 1
print("Number of palindrome words:", palindrome)
print("Words in reverse:")
for w in words:
    print(w[::-1])
