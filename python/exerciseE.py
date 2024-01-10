'''
Avni Gandhi
CIS 41A, Spring 2023
Unit E, Exercise E
'''

#if logic
scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]
moviename = input("Please enter a movie title: ")
if(moviename in scifi):
    print(moviename, "is a scifi movie.")
elif(moviename in comedy):
    print(moviename, "is a comedy movie.")
else:
    print("Sorry, I don't know what kind of movie", moviename, "is.")

#using range
for i in range(10, -1, -1):
    if(i % 2 == 0):
        print(i)

movies = {'The Wizard of Oz': 1939,
          'The Godfather': 1972,
          'Lawrence of Arabia': 1962,
          'Raging Bull': 1980}
for movie, year in sorted(movies.items()):
    print(movie, "was made in", year)



'''
Execution results:
Please enter a movie title: Moon
Moon is a scifi movie.
Please enter a movie title: Superbad
Superbad is a comedy movie.
Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.
10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939

'''
