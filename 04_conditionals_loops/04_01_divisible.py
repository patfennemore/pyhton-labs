'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
user_input = int(input("Choose a number between 1 and 1,000,000,000: "))
if user_input % 3 == 0:
    print(str(user_input) + " is divisible by 3")
else:
    print(str(user_input) + " is not divisible by 3")