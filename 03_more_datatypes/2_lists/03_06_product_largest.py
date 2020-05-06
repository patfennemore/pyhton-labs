'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''


user_input = input("Enter 10 numbers: ")
user_input_list = user_input.split()
user_input_list = [int(num) for num in user_input_list]

print("\n" + str(max(user_input_list)) + " is the largest number")


list_total = 0
for num in user_input_list:
    list_total += num

print("\n" + "The product of all the numbers is: " + str(list_total))