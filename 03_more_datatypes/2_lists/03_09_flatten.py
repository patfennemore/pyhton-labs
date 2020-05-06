'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flattened_list = []
x = -1

for l in starting_list:
    if x < 3:
        x += 1
        flattened_list.extend(starting_list[x])

print("flattened_list = " +str(flattened_list))