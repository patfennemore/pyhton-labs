'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}

unsorted_list = []

for key, value in input_dict.items():
    new_tuple = (key, value)
    unsorted_list.append(new_tuple)

sorted_list = sorted(unsorted_list, key=lambda element: element[-1])

print(sorted_list)
print(unsorted_list)
