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
# Problem 1 output
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
# Problem 2 output
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
# Problem 3 output
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













