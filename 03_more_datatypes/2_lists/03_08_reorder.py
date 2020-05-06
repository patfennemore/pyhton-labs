'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

# user input 10 numbers
user_input = input("Enter 10 numbers: ")

# split number into list
user_input_list = user_input.split()
# set start index to 0
position = -1
# increase position by 2 every loop
for num in user_input_list:
    if position <= 7:
        position += 2
        print(user_input_list[position])
        continue
position = 0
for num in user_input_list:
    if position >= -8:
        position -= 2
        print(user_input_list[position])
