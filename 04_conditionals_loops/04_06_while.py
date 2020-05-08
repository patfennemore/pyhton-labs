'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

count = 1

for number in range(1, 1001):
    while count == number:
        count += 1
        if number % 5 == 0:
            print(number)