'''
Avni Gandhi
CIS 41A, Spring 2023
Unit G, Problem G
'''
#part one
filepath = "States.txt"
file = open(filepath, "r")

maxPop = 0
maxAbbr = ""

for line in file:
    stateAbbr, region, population = line.split()

    if region == "Midwest" and int(population) > maxPop:
        maxPop = int(population)
        maxAbbr = stateAbbr

file.close()


print("Highest population state in the Midwest is:", maxAbbr, maxPop)

'''
Execution result:
Highest population state in the Midwest is: IL 12802000
'''

#part two
from collections import defaultdict
filepath = "USPresidents.txt"
file = open(filepath, "r")

statePresidents = defaultdict(list)

for line in file:
    stateBorn, presidentName = line.split()
    statePresidents[stateBorn].append(presidentName)

file.close()

maxState = " "
maxCount = 0

for state, presidents in statePresidents.items():
    if len(presidents) > maxCount:
        maxState = state
        maxCount = len(presidents)

print("The state with the most presidents is", maxState, "with", maxCount, "presidents:")
for president in statePresidents[maxState]:
    print(president)

'''
Execution result:
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
'''
#part three
mostPopulousStates = {'CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'}
presidentCount = {state: len(presidents) for state, presidents in statePresidents.items()}
usStatesPresidents = mostPopulousStates.intersection(presidentCount.keys())
print(len(usStatesPresidents), "of the", len(mostPopulousStates), "high population states have had presidents born in them:")
for state in sorted(usStatesPresidents):
    print(state, " ", presidentCount[state])

'''
Execution result:
8 of the 10 high population states have had presidents born in them:
CA   1
GA   1
IL   1
NC   2
NY   5
OH   7
PA   1
TX   2
'''
