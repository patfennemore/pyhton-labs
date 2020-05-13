'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

user_numbers = input("Please enter a list of numbers:")
user_numbers_list = list(user_numbers.split())
user_numbers_int = [int(string) for string in user_numbers_list]
user_numbers_sorted = sorted(user_numbers_int)
print("Sorted Numbers: " + str(user_numbers_sorted))

tuple_list = []

size = len(user_numbers_sorted)
count = 0
count_2 = 2

for number in user_numbers_sorted:
    if count_2 <= size:
        new_list = tuple(user_numbers_sorted[count:count_2])
        count += 2
        count_2 += 2
        tuple_list.append(new_list)
if size % 2 == 1:
    new_list_1 = list(user_numbers_sorted[-1:])
    new_list_1.append(0)
    tuple_list.append(tuple(new_list_1))
print(tuple_list)
