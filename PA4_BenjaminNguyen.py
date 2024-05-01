# Authors: Benjamin Nguyen
# Assignment: PA4
# Completed (or last revision): 04/29/2024
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Task 1: Text File Processing and Exception Handling
def task1():
    fname = input("Enter the file name: ")
    attempts = 0
    while attempts < 3:
        try:
            rfile = open(fname, 'r')
            break
        except FileNotFoundError:
            attempts += 1
            print("File not found. Please re-enter the file name.")
            fname = input("Enter file name: ")

    numOfLines = 0
    numOfWords = 0
    setOfWords = set()
    dictOfWords = {}
    for line in rfile:
        numOfLines += 1
        words = [word.strip(",.!?:;") for word in line.split()]
        i = 0
        while i < len(words):
            if words[i].isalpha():
                numOfWords += 1
                words[i] = words[i].lower()
                if words[i] in dictOfWords:
                    dictOfWords[words[i]] += 1
                else:
                    dictOfWords[words[i]] = 1
                i += 1
            else:
                words.pop(i)
        setOfWords.update(words)

    print(f"{fname} - The total number of lines are {numOfLines}, and the total number of words are {numOfWords}")
    sorted_dictOfWords = dict(sorted(dictOfWords.items(), key=lambda x:x[1], reverse=True))
    print(sorted_dictOfWords)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(sorted_dictOfWords)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    plt.close()
# Task 2: Operator Overloading
def task2():
    class Pair:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
        def __str__(self):
            return f"<{self.x}, {self.y}>"

        def __add__(self, other):
            return Pair(self.x + other.x, self.y + other.y)

        def __mul__(self, other):
            return Pair(self.x * other.x, self.y * other.y)

        def __truediv__(self, other):
            return Pair(self.x * self.y - other.x * other.y, self.x * other.x - self.y * other.y)
    # test case 1
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)
    print(p1)
    print(p2)
    print(p3)
    print(p1 + p2)
    print(p1 * p2)
    print(p1 / p2)
    print(p1 + p2 * p3)
    print(p1 * p2 / p3 + p1)
    # test case 2
    p4 = Pair()
    p5 = Pair(10, -2)
    p6 = Pair(7, 7)
    print()
    print(p4)
    print(p5)
    print(p6)
    print(p4 + p5)
    print(p5 * p6)
    print(p4 / p5)
    print(p4 + p5 * p6)
    print(p4 * p4 / p6 + p5)
# Task3: Inheritance
def task3():
    class Bicycle:
        def __init__(self, gear, speed):
            self.gear = gear
            self.speed = speed
        def applyBrake(self, decrement):
            self.speed -= decrement
        def speedUp(self, increment):
            self.speed += increment
        def __str__(self):
            return f"No of gears are {self.gear}\nspeed of bicycle is {self.speed}"
        def setSpeed(self, newValue):
            self.speed = newValue

    class MountainBike(Bicycle):
        def __init__(self, gear, speed, startHeight):
            super().__init__(gear, speed)
            self.seatHeight = startHeight
        def setHeight(self, newValue):
            self.seatHeight = newValue
        def getHeight(self):
            return self.seatHeight
        def applyBrake(self):
            self.setSpeed(0)
        def __str__(self):
            return f"{super().__str__()}\nseat height is {self.seatHeight}"
    # test case
    mb = MountainBike(3, 100, 25)
    print(mb)
    mb.applyBrake()
    print(mb)
    mb.setSpeed(20)
    mb.speedUp(30)
    mb.setHeight(30)
    print(mb.getHeight())
    print(mb)

def main():
    task1()
    task1()
    task2()
    task3()

main()
# Task 1 Output
"""
Enter the file name: Python.txt
Python.txt - The total number of lines are 12, and the total number of words are 128
{'the': 9, 'machine': 6, 'learning': 6, 'python': 5, 'is': 5, 'a': 5, 'of': 5, 'to': 5, 'learn': 4, 'and': 4, 'computer': 3, 'programming': 2, 'that': 2, 'from': 2, 'data': 2, 'into': 2, 'high': 1, 'level': 1, 'general': 1, 'purpose': 1, 'language': 1, 'design': 1, 'philosophy': 1, 'emphasizes': 1, 'code': 1, 'readability': 1, 'consistently': 1, 'ranks': 1, 'as': 1, 'one': 1, 'most': 1, 'popular': 1, 'languages': 1, 'field': 1, 'science': 1, 'uses': 1, 'statistical': 1, 'techniques': 1, 'give': 1, 'programs': 1, 'ability': 1, 'past': 1, 'experiences': 1, 'improve': 1, 'how': 1, 'they': 1, 'perform': 1, 'specific': 1, 'tasks': 1, 'you': 1, 'will': 1, 'steps': 1, 'necessary': 1, 'create': 1, 'successful': 1, 'application': 1, 'with': 1, 'scikit': 1, 'library': 1, 'making': 1, 'studying': 1, 'statistics': 1, 'step': 1, 'direction': 1, 'artificial': 1, 'intelligence': 1, 'program': 1, 'analyses': 1, 'learns': 1, 'predict': 1, 'outcome': 1, 'get': 1, 'ready': 1, 'dive': 1, 'world': 1, 'by': 1, 'using': 1}
Enter the file name: Python2.txt
Python2.txt - The total number of lines are 21, and the total number of words are 125
{'thy': 8, 'the': 7, 'to': 4, 'and': 4, 'by': 3, 'that': 2, 'might': 2, 'but': 2, 'his': 2, 'tender': 2, 'thou': 2, 'thine': 2, 'own': 2, 'self': 2, 'now': 2, 'in': 2, 'sonnets': 1, 'william': 1, 'shakespeare': 1, 'from': 1, 'fairest': 1, 'creatures': 1, 'we': 1, 'desire': 1, 'increase': 1, 'thereby': 1, 'rose': 1, 'never': 1, 'die': 1, 'as': 1, 'riper': 1, 'should': 1, 'time': 1, 'decease': 1, 'heir': 1, 'bear': 1, 'memory': 1, 'contracted': 1, 'bright': 1, 'eyes': 1, 'flame': 1, 'with': 1, 'fuel': 1, 'making': 1, 'a': 1, 'famine': 1, 'where': 1, 'abundance': 1, 'lies': 1, 'foe': 1, 'sweet': 1, 'too': 1, 'cruel': 1, 'art': 1, 'fresh': 1, 'ornament': 1, 'only': 1, 'herald': 1, 'gaudy': 1, 'spring': 1, 'within': 1, 'bud': 1, 'buriest': 1, 'content': 1, 'churl': 1, 'waste': 1, 'niggarding': 1, 'pity': 1, 'world': 1, 'or': 1, 'else': 1, 'this': 1, 'glutton': 1, 'be': 1, 'eat': 1, 'due': 1, 'grave': 1, 'thee': 1, 'when': 1, 'forty': 1, 'winters': 1, 'shall': 1, 'besiege': 1, 'brow': 1, 'dig': 1, 'deep': 1, 'trenches': 1, 'field': 1, 'proud': 1, 'livery': 1, 'so': 1, 'gazed': 1, 'on': 1}
"""
# Task2 Output
"""
<3, 2>
<1, 5>
<4, 3>
<4, 7>
<3, 10>
<1, -7>
<7, 17>
<21, -16>

<0, 0>
<10, -2>
<7, 7>
<10, -2>
<70, -14>
<20, 0>
<70, -14>
<-39, -2>
"""
# Task 3 Ouput
"""
No of gears are 3
speed of bicycle is 100
seat height is 25
No of gears are 3
speed of bicycle is 0
seat height is 25
30
No of gears are 3
speed of bicycle is 50
seat height is 30
"""