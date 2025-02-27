words = ["apple", "banana", "apple", "orange", "banana", "banana"]
wordcount = {}

for word in words:
    if word in wordcount:
        word_count[word] += 1
    else:
        wordcount[word] = 1

duplicates = {}
for word in wordcount:
    if wordcount[word] > 1:
        duplicates[word] = wordcount[word]

print(duplicates)
