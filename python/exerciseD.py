'''
Avni Gandhi
CIS 41A Spring 2023
Unit D, Exercise D
'''

#dictionary basics
fruits_desserts = {'apple':'sauce',
           'peach':'cobbler',
           'carrot':'cake',
           'strawberry':'sorbet',
           'banana':'cream pie'}
fruits_desserts['mango'] = 'sticky rice'
fruits_desserts.update({'strawberry': 'shortcake'})
del fruits_desserts['carrot']
print("apple dessert is:", fruits_desserts['apple'])
print("banana dessert exists:", 'banana' in fruits_desserts) 
print("pear dessert exists:", 'pear' in fruits_desserts) 
print(fruits_desserts.keys())
print(fruits_desserts.values())
print(fruits_desserts.items())

#combining dictionaries
capitols1 = {'Alabama': 'Montgomery',
             'Alaska': 'Juneau',
             'Arizona':'Phoenix',
             'Arkansas':'Little Rock',
             'California':'Sacramento'}
capitols2 = {'California':'Sac.',
             'Colorado':'Denver',
             'Connecticut':'Hartford'}
capitols1.update(capitols2)
print("sorted state capitals:", sorted(capitols1.values()))

#sets basics
class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
class1.add('John')
print("students in both classes:", sorted(class1.intersection(class2)))
print("all students:", sorted(class1.union(class2)))
print("Sasha is in class1:", 'Sasha' in class1)

'''
Execution results:

apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
sorted state capitals: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
students in both classes: ['Audry', 'Migel', 'Tanya']
all students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False
'''
