'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

user_input = input("Write a sentence: ")

split_user_input = list(user_input.split())

my_dict = {}

for word in split_user_input:
    # print(split_user_input.count(word))
    my_dict[word] = 0
    my_dict[word] += split_user_input.count(word)

current_biggest_value = 0

for key in my_dict:
    value = my_dict[key]
    if value > current_biggest_value:
        current_biggest_value = value
        print(list(my_dict.keys())[list(my_dict.values()).index(value)])



