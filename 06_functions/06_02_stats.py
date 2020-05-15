'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(user_list):

    max_found = max(user_list)
    min_found = min(user_list)
    sum_found = sum(user_list)
    avg = sum_found / len(user_list)

    user_list = max_found, min_found, sum_found, avg

    return print(user_list)


stats(example_list)
