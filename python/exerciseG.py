'''
Avni Gandhi
CIS 41A, Spring 2023
Unit G, Exercise G
'''
import csv
#part one
with open("ZenOfPython.txt", "w") as file:
    file.write("Beautiful is better than ugly.\n")
    file.write("Explicit is better than implicit.\n")

with open("ZenOfPython.txt", "a") as file:
    file.write("Readability counts.\n")
    file.write("If the implementation is hard to explain, it's a bad idea.")

with open("ZenOfPython.txt", "r") as file:
    print(file.read())

'''
Execution results:

Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
'''
#part two
print()
information = {}
with open("Cities.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        city = row["City"]
        state = row["State"]
        population = int(row["Population"])
        key = (city, state)
        information[key] = population

    for key, value in information.items():
        print(f"{key[0]} {key[1]} {value}")

print()
city = input("Please enter a city: ")
state = input("Please enter a state: ")

newkey = (city, state)
if newkey in information:
    print(f"{city}, {state} has a population of {information[newkey]}")

'''
Execution results:

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin
Please enter a state: California
Dublin, California has a population of 46036
'''
    
