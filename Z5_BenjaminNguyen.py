# Authors: Benjamin Nguyen
# Assignment: Z5 Substitute
# Completed (or last revision): 02/22/2024
"""
# Problem 1
def hideCharacters(strToReplace):
    return len(strToReplace) * "*"

print(hideCharacters("secret"))
print(hideCharacters("HI"))
"""

"""
# Problem 1 Output
******
**
"""

"""
# Problem 2
def firstInSet(strSet, searchChar):
    if strSet == "" or searchChar == "":
        return -1
    else:
        for ch in searchChar:
            index = strSet.find(ch)
            if index >= 0:
                return index
        else:
            return -1

print(firstInSet("spring", "aeiou"))
print(firstInSet("", "aeiou"))
print(firstInSet("bc", "aeiou"))
"""

"""
# Problem 2 Output
3
-1
-1
"""

"""
# Problem 3
def printCalendar(firstDayCol, numOfDays):
    print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")
    dayCount = 1
    print("   " * firstDayCol, end="")
    daysInWeek = 7 - firstDayCol
    while dayCount <= numOfDays:
        for i in range(daysInWeek):
            if dayCount <= numOfDays:
                print(f"{dayCount:2d}", end=" ")
                dayCount += 1
            else:
                print("  ", end=" ")
        print()
        daysInWeek = 7

def main():
    days = int(input("Number of days: "))
    print()
    weekday = int(input("Weekday of first day (0 = Sunday): "))
    print()
    printCalendar(weekday, days)
main()
"""

"""
# Problem 3 Output
Number of days: 31

Weekday of first day (0 = Sunday): 2

Su Mo Tu We Th Fr Sa
       1  2  3  4  5 
 6  7  8  9 10 11 12 
13 14 15 16 17 18 19 
20 21 22 23 24 25 26 
27 28 29 30 31       

Number of days: 30

Weekday of first day (0 = Sunday): 6

Su Mo Tu We Th Fr Sa
                   1 
 2  3  4  5  6  7  8 
 9 10 11 12 13 14 15 
16 17 18 19 20 21 22 
23 24 25 26 27 28 29 
30                   
"""

"""
# Problem 4
# (a) - local variables: total, avg, i, and iSquared
# (b) - The program prints "4 16"
# (c):
y = 8
def main() :
    x = 4 # Q1: what is the scope of this x? - local to main() function 
    x = mystery(x + 1)
    print(s)
def mystery(x) : # Q2: what is the scope of this x? - local to mystery() function 
    s = 0
    for i in range(x) : # Q3: what is the scope of i? - local to mystery() function
        x = i + 1
        s = s + x
    return s
main() # Q4: in above code, which line defines a global variable? - 1
"""

"""
# Problem 5
# (a)
def main() :
    print(blackBox(4))
def blackBox(a) :
    if a <= 0 :
        val = 1
    else :
        val = a + blackBox(a - 2)
    return val
main()

# (b)
def printBoxes(n):
    if n == 0:
        return
    print("[]", end=" ")
    printBoxes(n - 1)

n = int(input("Enter the number of box shapes or -1 to exit: "))
while n >= 0:
    printBoxes(n)
    print()
    n = int(input("Enter the number of box shapes or -1 to exit: "))
"""

"""
# Problem 5 Output
(a): 7
(b):
Enter the number of box shapes or -1 to exit: 0

Enter the number of box shapes or -1 to exit: 5
[] [] [] [] [] 
Enter the number of box shapes or -1 to exit: -1
"""