#Avni Gandhi
#1/28/2023
#Python 3.11.1
#Description: Program to convert any given number of total cents
#into the correct number of quarters, dimes, nickels, and pennies.

#user enters input
totalCents = int(input('enter total cents:'))
quarters = int(totalCents/25)

if quarters > 0:
    print('you have', quarters,'quarters')
    totalCents = totalCents - quarters*25

dimes = int(totalCents/10)
if dimes > 0:
    print('you have', dimes,'dimes')
    totalCents = totalCents - dimes*10

nickels = int(totalCents/5)
if nickels > 0:
    print('you have', nickels,'nickels')
    totalCents = totalCents - nickels*5

pennies = int(totalCents/1)
if pennies > 0:
    print('you have', pennies,'pennies')
    
'''
>>>
=================== RESTART: /Users/avnigandhi/python/p13.py ===================
enter total cents:66
you have 2 quarters
you have 1 dimes
you have 1 nickels
you have 1 pennies
>>>
'''
