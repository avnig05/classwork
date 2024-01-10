'''
Avni Gandhi
CIS 41A, Spring 2023
Unit H, Exercise H
'''

class StateData:
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population

    def __str__(self):
        return self.name

    def displayState(self):
        print(f"{self.name}")
        print(f"{self.name} ({self.abbreviation}) is in the {self.region} and has a population of {self.population}")



s1 = StateData("California", "CA", "West", 39250000)
s1.displayState()

'''
Execution results:
California
California (CA) is in the West and has a population of 39250000
'''
class StateData2:
    def __init__(self, name):
        self.name = name

    def setRegion(self, region):
        self.region = region

    def getRegion(self):
        return self.region
s2 = StateData2("California")
s2.setRegion("West")
s2.pop = 3925000

print(s2.name)
print(s2.getRegion())
print(s2.region)
print(s2.pop)

'''
Execution results:
California
West
West
3925000
'''

class StateData2:
    def __init__(self):
        self.public = "Public"
        self._protected = "protected"
        self.__private = "Private"
test = StateData2()
print(test.public)
print(test._protected)
print(test.__private)

'''
Execution results:
Public
protected
Traceback error
'''

