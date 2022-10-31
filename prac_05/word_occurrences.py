"""
CP1404 | Practical 05 - word_occurrences  | Liam Eime
Program to count the occurrences of words in a string
Estimate: 30 minutes
Actual: 26.5 minutes
"""

text = input("Enter a string of words: ")
word_to_count = {}

for word in text.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max((len(word) for word in list(word_to_count.keys())))

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
