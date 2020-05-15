'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def print_text(user_input):
    print(user_input)
    return user_input


def multiply_text(user_input):
    print_text(user_input*3)
    return user_input


def new_line(user_input):
    multiply_text(user_input + "\n")
    return user_input


new_line("Hello World")
