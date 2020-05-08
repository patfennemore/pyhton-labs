'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
user_input = int(input("Please enter a number: "))
month_dict = {}
count = 0

import calendar
for month in range(1, 13):
    count += 1
    month_dict[calendar.month_name[month]] = count

if user_input <= 12:
    for key, value in month_dict.items():
        if value == user_input:
            print(key)
else:
    print("Other")
