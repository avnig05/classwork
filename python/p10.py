#Avni Gandhi
#1/23/2023
#Python 3.11.1
#Description: a program which asks user for a student's grade
#as a percent, and then returns their letter grade

#ask the user to enter grade as percent
percent = float(input('please enter grade as a percent:'))

#validate input
if percent < 0 or percent > 100:
    print('error, percent must be between 0 and 100')
    percent = float(input('enter value between 0 and 100:'))

#show the correct letter grade based on the percent
if percent >= 90:
    print('the grade is "A" ')
if percent >= 80 and percent < 90:
    print('the grade is "B" ')
if percent >= 70 and percent < 80:
    print('the grade is "C" ')
if percent >= 60 and percent < 70:
    print('the grade is "D" ')
if percent < 60:
    print('the grade is "F" ')
    
'''
>>>
=================== RESTART: /Users/avnigandhi/python/p10.py ===================
please enter grade as a percent:99
the grade is "A"
>>>
'''
