'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
user_input = input("Please type a sentence: ")
user_words = list(user_input.split())

count = 0
new_list = []

for word in user_words:
    if count == 0:
        new_list.append(tuple(word))
    count += 1
    if count >= 2:
        new_list.append(tuple(word))
        result_list = list(new_list)

print(result_list)