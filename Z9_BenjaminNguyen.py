# Authors: Benjamin Nguyen
# Assignment: Z9
# Completed (or last revision): 04/20/2024

# Problem 1
def task1():
    class Bug:
        def __init__(self, pos=None):
            if pos is None:
                self.pos = 0
            else:
                self.pos = pos

        def reset(self):
            self.pos = 0

        def up(self):
            if self.pos + 10 == 100:
                print("The bug has reached the top of the pole.")
                self.reset()
            else:
                self.pos += 10

        def getPosition(self):
            return self.pos

    # Test run 1
    bug = Bug(80)
    print(f"The bug's current position is {bug.getPosition()}.")
    bug.up()
    print(f"The bug's current position is {bug.getPosition()}.")
    bug.up()
    print(f"The bug's current position is {bug.getPosition()}.")

# Problem 2
def task2():
    class Trafficlight:
        def __init__(self, color=None):
            if color is None:
                self.color = "red"
            else:
                self.color = color

        def get_color(self):
            return self.color

        def next(self):
            if self.color == "green":
                self.color = "yellow"
            elif self.color == "yellow":
                self.color = "red"
            elif self.color == "red":
                self.color = "green"

    # Test run 2
    streetlight = Trafficlight()
    print()
    print(f"The current color of the traffic light is {streetlight.get_color()}.")
    streetlight.next()
    print(f"The next color of the traffic light is {streetlight.get_color()}.")

# Problem 3
def task3():
    class Lock:
        def __init__(self, code=None):
            if code is None:
                self.code = "0000"
                self.cur_combination = ""
            else:
                self.code = code
                self.cur_combination = ""
        def push(self, button):
            self.cur_combination += str(button)
        def open(self):
            validate_combination = self.cur_combination == self.code
            self.cur_combination = ""
            return validate_combination

    # Test run 3
    door_lock = Lock("1234")
    door_lock.push(1)
    print()
    print(f"The current combination entered: {door_lock.cur_combination}")
    door_lock.push("2")
    print(f"The current combination entered: {door_lock.cur_combination}")
    door_lock.push('3')
    print(f"The current combination entered: {door_lock.cur_combination}")
    door_lock.push(4)
    print(f"The current combination entered: {door_lock.cur_combination}")
    print(f"Attempting to unlock...{door_lock.open()}")
    print(f"The current combination entered: {door_lock.cur_combination}")

def main():
    task1()
    task2()
    task3()

main()
"""
The bug's current position is 80.
The bug's current position is 90.
The bug has reached the top of the pole.
The bug's current position is 0.

The current color of the traffic light is red.
The next color of the traffic light is green.

The current combination entered: 1
The current combination entered: 12
The current combination entered: 123
The current combination entered: 1234
Attempting to unlock...True
The current combination entered: 
"""