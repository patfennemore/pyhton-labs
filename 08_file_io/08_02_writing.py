'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []
with open("words.txt", "r") as fin:
    for word in fin:
        words.append(word)
words_ordered = sorted(words, reverse=True)

with open("words_reverse.txt", "w") as fout:
    fout.write("".join(words_ordered))
