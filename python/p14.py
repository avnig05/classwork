#Avni Gandhi
#1/28/2023
#Python 3.11.1
#Description: program that asks the user for day and
#month of a birthday and then tells the Zodiac signs
#that will be compatible with that birthday.

#ask user for birth month and date
day = int(input('Please enter date of birth:'))
month = int(input('Please enter month of birth:'))

#determine what zodiac sign user is
if(month == 3 and day >= 21 or month == 4 and day <= 19):
    print("Your zodiac sign is Aries")
    
if(month == 4 and day >= 20 or month == 5 and day <= 20):
    print("Your zodiac sign is Taurus")

if(month == 5 and day >= 21 or month == 6 and day <= 21):
    print("Your zodiac sign is Gemini")

if(month == 6 and day >= 22 or month == 7 and day <= 22):
    print("Your zodiac sign is Cancer")

if(month == 7 and day >= 23 or month == 8 and day <= 22):
    print("Your zodiac sign is Leo")

if(month == 8 and day >= 23 or month == 9 and day <= 22):
    print("Your zodiac sign is Virgo")

if(month == 9 and day >= 23 or month == 10 and day <= 23):
    print("Your zodiac sign is Libra")

if(month == 10 and day >= 24 or month == 11 and day <= 21):
    print("Your zodiac sign is Scorpio")

if(month == 11 and day >= 22 or month == 12 and day <= 21):
    print("Your zodiac sign is Sagittarius")

if(month == 12 and day >= 22 or month == 1 and day <= 19):
    print("Your zodiac sign is Capricorn")

if(month == 1 and day >= 20 or month == 2 and day <= 18):
    print("Your zodiac sign is Aquarius")

if(month == 2 and day >= 19 or month == 3 and day <= 20):
    print("Your zodiac sign is Pisces")

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p14.py ===================
Please enter date of birth:18
Please enter month of birth:5
Your zodiac sign is Taurus
>>>
'''
