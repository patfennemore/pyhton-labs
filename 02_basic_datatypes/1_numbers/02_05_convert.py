'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# 1)
int_original = 5
float_example = float(int_original)

print(float_example)

# 2)
int_example = int(float_example)

print(int_example)

# 3)
floor_division = float_example//int_example

print(floor_division)

# 4)
first_user_input = float(input("Please enter any number: "))
second_user_input = float(input("Please enter another number: "))

multiplication_result = first_user_input*second_user_input

print(multiplication_result)