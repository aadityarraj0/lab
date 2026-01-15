words = open("sample.txt").read().lower().split()

count = {}
for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

sorted_words = sorted(count.items(), key = lambda x: x[1], reverse=True)

print("Top 10 words: ")
for word, freq in sorted_words[:10]:
    print(word, ":", freq)



