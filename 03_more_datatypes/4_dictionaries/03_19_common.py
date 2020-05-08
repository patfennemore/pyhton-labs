'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

dict_result = dict(dict_1)
dict_result.update(dict_2)

for key_1, value_1 in dict_1.items():
    for key_2, value_2 in dict_2.items():
        if key_1 == key_2:
            dict_result[key_1] = (value_1 + value_2)

print(dict_result)