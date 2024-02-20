#Avni Gandhi
#2/15/2023
#Python 3.11.1
#Description: a program that asks the user to input a sentence and then counts
#how many times the chosen letter appears in the sentence

count1 = 0
count2 = 0
sentence = input("Please enter a sentence:")
letter1 = input("Please enter letter 1:")
letter2 = input("Please enter letter 2:")

for i in range(0, len(sentence), 1):
    if sentence[i] == letter1:
        count1+=1
    if sentence[i] == letter2:
        count2+=1
print("The letter", letter1, "occurs", count1,"time(s)")
print("The letter", letter2, "occurs", count2,"time(s)")

'''
=================== RESTART: /Users/avnigandhi/python/p25.py ===================
Please enter a sentence:hello world
Please enter letter 1:o
Please enter letter 2:l
The letter o occurs 2 time(s)
The letter l occurs 3 time(s)
'''
