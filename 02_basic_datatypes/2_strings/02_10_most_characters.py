'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

sentence = input("Please enter 3 words with spaces in between: ")
word_list = sentence.split()

first_word = word_list[0]
second_word = word_list[1]
third_word = word_list[2]

first_word_length = len(word_list[0])
second_word_length = len(word_list[1])
third_word_length = len(word_list[2])

print(str(first_word_length) + ", " + str(first_word))
print(str(second_word_length) + ", " + str(second_word))
print(str(third_word_length) + ", " + str(third_word))

maximum_char = max(len(w)for w in word_list)
print("Longest word in the list has",maximum_char, "characters")

if len(word_list) == maximum_char:
       print(word_list)




