#Задача K
headings = []
for _ in range(int(input())):
    headings.append(input())
word = input()
for heading in headings:
    if word.lower() in heading.lower():
        print(heading)