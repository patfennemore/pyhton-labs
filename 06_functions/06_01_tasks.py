'''

Write a script that completes the following tasks.

'''


def four_or_seven(number):
    result = bool(number % 4 == 0 or number % 7 == 0)
    return result


def four_and_seven(number):
    result = bool(number % 4 == 0 and number % 7 == 0)
    return result


user_input = int(input("Enter a number between 1 and 1000 000 000: "))

four_or_seven_result = four_or_seven(user_input)
four_and_seven_result = four_and_seven(user_input)

print(four_or_seven_result)
print(four_and_seven_result)
