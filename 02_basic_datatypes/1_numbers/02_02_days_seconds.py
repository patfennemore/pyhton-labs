'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))

seconds = days*24*60*60

print(str(seconds) + " seconds")

