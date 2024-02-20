#Avni Gandhi
#2/4/2023
#Python 3.11.1
#Description: program to determine which one the following gives you
#more money
penny = 1
million = 1000000
for day in range (0, 30, 1):
    penny = penny * 2

difference = penny - million
difference = '{:,}'.format(difference)
print("On the 30th day you will have",difference, "more pennies")


'''
>>>
=================== RESTART: /Users/avnigandhi/python/p21.py ===================
On the 30th day you will have 1,072,741,824 more pennies
>>>
'''
