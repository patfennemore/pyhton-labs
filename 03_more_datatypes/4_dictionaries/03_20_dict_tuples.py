'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}

sorted_values = sorted(input_dict.values())

new_list = []

for sorted_value in sorted_values:
    for key, value in input_dict.items():
        if sorted_value == value:
            new_tuple = (key, value)
            new_list.append(new_tuple)

print(new_list)