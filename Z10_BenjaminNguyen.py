# Authors: Benjamin Nguyen
# Assignment: Z10
# Completed (or last revision): 04/24/2024
# Problem 1
class Player:
    def __init__(self):
        self._name = ""
        self._salary = 0.0
    def setName(self, theName):
        self._name = theName
    def setSalary(self, theSalary):
        self._salary = theSalary
    def getName(self):
        return self._name
    def getSalary(self):
        return self._salary
    def display(self):
        print(f"{self._name} has a salary of {self._salary}.")
class BaseballPlayer(Player):
    def __init__(self, atBats=0, hits=0):
        super().__init__()
        self._atBats = atBats
        self._hits = hits
        self._homeRuns = 0
    def setHomeRuns(self, number):
        self._homeRuns = number
    def getBattingAvg(self):
        return self._hits / self._atBats
    def display(self):
        print(f"{self.getName()} has a salary of {self.getSalary()}\nNumber of at bats: {self._atBats}\nNumber of hits: {self._hits}\nNumber of home runs: {self._homeRuns}")

# Problem 2
class Critter:
    def __init__(self):
        self.position = 0
    def act(self):
        self.position += 10
    def display(self):
        print(f"The position is {self.position}")

class Bug(Critter):
    def __init__(self):
        super().__init__()
        self.legs = 6
        self.canHop = True

    def act(self):
        if self.canHop:
            super().act()
            super().act()
        else:
            super().act()
    def display(self):
        super().display()
        print(f"This bug has {self.legs} legs and its ability to hop is {self.canHop}")
    def setHop(self, status):
        self.canHop = status

class LadyBug(Bug):
    def __init__(self):
        super().__init__()
        self.canFly = True
    def act(self):
        super().act()
    def display(self):
        super().display()
        print(f"This ladybug's ability to fly is {self.canFly}")


def main():
    # Problem 1 testing
    man = Player()
    man.display()
    man.setName("John")
    man.setSalary(1000)
    man.display()
    print()
    baseman = BaseballPlayer(10, 5)
    baseman.display()
    baseman.setHomeRuns(2)
    baseman.setName("Bob")
    baseman.setSalary(5000)
    baseman.display()
    print(f"The batting average is {baseman.getBattingAvg()}")
    # Problem 2 testing
    critters = []
    critters.append(Bug())
    critters.append(LadyBug())
    critters.append(Critter())
    bug2 = Bug()
    bug2.setHop(False)
    critters.append(bug2)
    for c in critters:
        c.act()
        c.display()
        print()

main()
"""
 has a salary of 0.0.
John has a salary of 1000.

 has a salary of 0.0
Number of at bats: 10
Number of hits: 5
Number of home runs: 0
Bob has a salary of 5000
Number of at bats: 10
Number of hits: 5
Number of home runs: 2
The batting average is 0.5
The position is 20
This bug has 6 legs and its ability to hop is True

The position is 20
This bug has 6 legs and its ability to hop is True
This ladybug's ability to fly is True

The position is 10

The position is 10
This bug has 6 legs and its ability to hop is False
"""