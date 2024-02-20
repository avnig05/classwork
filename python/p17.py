#Avni Gandhi
#2/4/2023
#Python 3.11.1
#Description: program that computes the tuition in ten years and displays
#a table of the years and tuition costs.

cost = 10000
increase = 1.05
year = 1

for year in range(1, 11,1):
    print("Year %2i" %year, "     Tuition", round(cost))
    cost = cost * increase
    year += 1

'''
>>>
=================== RESTART: /Users/avnigandhi/python/p17.py ===================
Year  1      Tuition 10000
Year  2      Tuition 10500
Year  3      Tuition 11025
Year  4      Tuition 11576
Year  5      Tuition 12155
Year  6      Tuition 12763
Year  7      Tuition 13401
Year  8      Tuition 14071
Year  9      Tuition 14775
Year 10      Tuition 15513
>>>
'''
