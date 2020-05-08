'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input = input("Please enter a word: ")

user_input_char = []
my_dict = {}

for char in user_input:
    user_input_char.append(char)
    my_dict[char] = user_input_char.count(char)
del my_dict[" "]

print("result = " + str(my_dict))