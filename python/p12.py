#Avni Gandhu
#1/28/2023
#Python 3.11.1
#Description: A program to determine if the user can vote

#ask user for input
age = int(input('please enter your age:'))
citizen = input('are you are citizen? (y/n)')
register = input('are you registered? (y/n)')

#check if user can vote

if age >= 18 and citizen == 'y' and register == 'y':
    print("Congratulations, you can vote!")

#if they can't vote
else:
    if age < 18:
        print("You must be over the age of 18")
    if citizen == 'n':
        print("You must be a citizen to vote")
    if register == 'n':
        print("You must be registered to vote")

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p12.py ===================
please enter your age:20
are you are citizen? (y/n)y
are you registered? (y/n)n
You must be registered to vote
>>>
'''
