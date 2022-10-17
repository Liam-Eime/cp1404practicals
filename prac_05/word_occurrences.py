"""
CP1404 | Practical 05 - word_occurrences  | Liam Eime
Program to count the occurrences of words in a string
Estimate: 30 minutes
Actual:
"""

string = str(input("Enter a string of words: "))
word_to_count = {}
for word in string.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(word_to_count):
    print(f"{word} : {word_to_count[word]}")
