'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def listtoDict(tup):
    op = dict(tup)
    return op


unsorted_words = {}

with open("words.txt", "r") as fin:
    for word in fin:
        unsorted_words[f"{word.rstrip()}"] = (len(word) - 1)

unsorted_list = []

for word, length in unsorted_words.items():
    new_tuple = (word, length)
    unsorted_list.append(new_tuple)

sorted_list = sorted(unsorted_list, key=lambda element: element[-1])
sorted_dict = listtoDict(sorted_list)

values_view = sorted_dict.values()
value_iterator = iter(values_view)
first_value = next(value_iterator)
last_word, last_word_length = sorted_list[-1]

shortest_words = []
longest_words = []

for word, length in sorted_dict.items():
    if length == first_value:
        shortest_words.append(word)
    if length == last_word_length:
        longest_words.append(word)

print(f"The shortest words are {shortest_words}")
print(f"The longest words are {longest_words}")
print(f"There are {len(sorted_dict)} words in the dictionary")
