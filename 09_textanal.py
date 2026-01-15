text = input("Enter a paragraph:\n")

text_lower = text.lower()
words = text_lower.split()

total_words = len(words)

word_frequency = {}
for word in words:
    word = word.strip(".,!?")
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

longest_word = ""
for word in words:
    word = word.strip(".,!?")
    if len(word) > len(longest_word):
        longest_word = word

sentences = 0
for char in text:
    if char in ".!?":
        sentences += 1

total_characters = len(text)

print("\n--- Text Analysis Results ---")
print("Total words:", total_words)
print("Total sentences:", sentences)
print("Total characters:", total_characters)
print("Longest word:", longest_word)

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)
