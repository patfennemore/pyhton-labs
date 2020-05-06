'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

list_ = list(dict.fromkeys(list_))
print(list_)