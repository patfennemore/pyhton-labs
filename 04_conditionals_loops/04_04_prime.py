'''
Print out every prime number between 1 and 100.

'''

for number in range(1, 101):
    if number > 1:
        for itself in range(2, number):
            if (number % itself) == 0:
                break
        else:
            print(number)