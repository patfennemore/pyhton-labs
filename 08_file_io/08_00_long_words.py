'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

twenty_char = []

with open("words.txt", "r") as fin:
    for word in fin:
        if len(word) >= 21:
            twenty_char.append(word.rstrip())

print(twenty_char)
