#Avni Gandhi
#2/14/2023
#Python 3.11.1
#Description: A program to let a child practice their arithmetic skills

import random
while True:
    math = int(input("Would you like to add(1), subtract(2), or multiply(3);"))
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    if (math == 1):
        answer = int(input("What is %i + %i:" %(num1, num2)))
        while(answer != (num1+num2)):
            answer = int(input("That is incorrect. What is %i + %i equal to?" %(num1,num2)))
    if (math == 2):
        answer = int(input("What is %i - %i:" %(num1, num2)))
        while(answer != (num1-num2)):
            answer = int(input("That is incorrect. What is %i - %i equal to?" %(num1,num2)))
    if (math == 3):
        answer = int(input("What is %i * %i:" %(num1, num2)))
        while(answer != (num1*num2)):
            answer = int(input("That is incorrect. What is %i * %i equal to?" %(num1,num2)))
    repeat = int(input("Correct! Would you like to try again? (yes(1), no(2)):"))
    if(repeat == 2):
        break
print("Thank you for playing!")

'''
=================== RESTART: /Users/avnigandhi/python/p23.py ===================
Would you like to add(1), subtract(2), or multiply(3);3
What is 6 * 6:33
That is incorrect. What is 6 * 6 equal to?36
Correct! Would you like to try again? (yes(1), no(2):1
Would you like to add(1), subtract(2), or multiply(3);1
What is 3 + 4:7
Correct! Would you like to try again? (yes(1), no(2)):2
Thank you for playing!
'''

