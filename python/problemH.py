'''
Avni Gandhi
CIS 41A, Spring 2023
Unit H, Problem H
'''
import pickle
class BritCoins:
    __coinValues = {"pound":240, "shilling":12, "penny":1}
    def __init__(self, **kwargs):
        self.totalPennies = 0
        for coinType, quantity in kwargs.items():
            coinValue = self.__coinValues.get(coinType, 0)
            self.totalPennies += coinValue * quantity
            
    def __add__(self, other):
       total = self.totalPennies + other.totalPennies
       return BritCoins(penny = total)

    def __sub__(self, other):
       total = self.totalPennies - other.totalPennies
       return BritCoins(penny = total)       

    def __str__(self):
        pound = self.totalPennies // self.__coinValues["pound"]
        shilling = (self.totalPennies % self.__coinValues["pound"]) // self.__coinValues["shilling"]
        penny = (self.totalPennies % self.__coinValues["shilling"]) // self.__coinValues["penny"]
        return f"{pound} pounds {shilling} shillings {penny} pennies"

c1 = BritCoins(pound = 4, shilling = 24, penny = 3)
print(c1)
c2 = BritCoins(pound = 3, shilling = 4, penny = 5)
print(c2)
c3 = c1 + c2
print(c3)
c4 = c1 - c2
print(c4)
print()

with open('BritCoins.pickle', 'wb') as file:
    pickle.dump(c4, file)

with open('BritCoins.pickle', 'rb') as file:
    unpickled_c4 = pickle.load(file)
print(unpickled_c4)

'''
Execution result:
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

1 pounds 19 shillings 10 pennies
'''
