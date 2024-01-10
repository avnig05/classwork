'''
Avni Gandhi
CIS 41A, Spring 2023
Unit D, Problem D
'''
from collections import namedtuple
#list comprehension
trianglenum = []
for i in range(1,11,1):
    trianglenum.append(i*(i+1)/2)

print("First 10 Triangle numbers:\n", trianglenum)

#sets
class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
class3 = {'Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'}
print("Students in all three classes:", sorted(class1.intersection(class2, class3)))
print("All students:", sorted(class1.union(class2, class3)))
print("Students in class1 but not class2 or class3:", sorted(class1 - class2 - class3))
print("Students in class2 but not class1:", sorted(class2 - class1))

#tuples
movie = ("Casablanca", "1942", "romantic drama")
title, year, genre = movie
print("The genre of my favorite movie is:", genre)
moviestars = namedtuple('moviestars', ['title','year', 'genre', 'stars'])
favoritemovie = moviestars("Casablanca", "1942", "romantic drama", ["Humphrey Bogart", "Ingrid Bergman"])
favoritemovie.stars.append("Claude Rains")
print("My favorite star is:", favoritemovie.stars[1])
print(favoritemovie)


'''
First 10 Triangle numbers:
[1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0]
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
Students in class2 but not class1: ['Hiroto', 'Sasha']
The genre of my favorite movie is: romantic drama
My favorite star is: Ingrid Bergman
moviestars(title='Casablanca', year='1942', genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''
