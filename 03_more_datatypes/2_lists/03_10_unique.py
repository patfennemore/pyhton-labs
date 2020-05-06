'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

original_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# count how many times an item in the list appears
unique_list = []

for obj in original_list:
    if original_list.count(obj) == 1:
        unique_list.append(obj)

print("unique_list = " + str(unique_list))