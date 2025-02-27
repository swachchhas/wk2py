sentence = input("Enter a sentence: ")
words = sentence.split()

for i in range(1, len(words), 2):
    words[i] = words[i][::-1]

newsentence = " ".join(words)
print(newsentence)
