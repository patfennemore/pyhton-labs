'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

user_number = int(input("Enter a number: "))

count = 0

for number in range(1, 1000000001):
    while number <= user_number:
        count += 1
        if count == user_number:
            break
    break

print(user_number)