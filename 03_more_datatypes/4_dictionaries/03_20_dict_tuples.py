'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}
input_dict_sorted = {}

sorted_list_values = sorted(input_dict.values())

for sorted_list_value in sorted_list_values:
    for key, value in input_dict.items():
        if sorted_list_value == value:
            input_dict_sorted[key] = value

result_list_1 = []
result_list = []

for key, value in input_dict_sorted.items():
    result_list_1.append(key)
    result_list_1.append(value)
    new_tuple = tuple(result_list_1)
    result_list.append(new_tuple)
    result_list_1.clear()
print(result_list)