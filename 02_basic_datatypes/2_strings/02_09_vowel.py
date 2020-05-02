'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
count = 0
for i in sentence.lower():
    if i in "aeiou":
        count += 1
print(str(count)+ " Vowels in sentence")

