#Задача E
from sys import stdin

data = [string.strip().split() for string in stdin]
words = []
for line in data:
    words.extend(line)
for word in sorted(set(words)):
    if word.lower() == word.lower()[::-1]:
        print(word)