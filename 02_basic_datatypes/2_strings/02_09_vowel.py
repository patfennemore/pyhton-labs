'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
vowels = 0
for i in sentence:
      if(i == 'a' or i == 'e' or i=='i' or i=='o' or i=='u'):
            vowels = vowels + 1
print("Number of vowels are: " + str(vowels))



