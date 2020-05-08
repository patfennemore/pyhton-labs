'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

my_dict = {}

n = 0

for n in range(0, 10):
    n += 1
    my_dict[n] = n*n

print(my_dict)
