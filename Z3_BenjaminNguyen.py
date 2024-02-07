# Authors: Benjamin Nguyen
# Assignment: Z3 Substitute
# Completed (or last revision): 02/10/2024
"""
# Problem 1
piePrice = float(input("Enter the price of the pie: $"))
if piePrice >= 10.00:
    print("The pie's discounted price is $%.2f" % (piePrice - 3.14))
else:
    print("The pie's discounted price is $%.2f" % (piePrice - 1.00))
"""
"""
# Problem 1 outputs
Enter the price of the pie: $9.99
The pie's discounted price is $8.99

Enter the price of the pie: $21.14
The pie's discounted price is $18.00
"""
"""
# Problem 2
x1, y1 = float(input("Enter the 1st x coordinate: ")), float(input("Enter the 1st y coordinate: "))
x2, y2 = float(input("Enter the 2nd x coordinate: ")), float(input("Enter the 2nd y coordinate: "))
if x1 == x2:
    print("The line is vertical.")
else:
    print("The line is not vertical.")
"""
"""
# Problem 2 outputs
Enter the 1st x coordinate: 1
Enter the 1st y coordinate: -100
Enter the 2nd x coordinate: 1
Enter the 2nd y coordinate: 100
The line is vertical.

Enter the 1st x coordinate: 0
Enter the 1st y coordinate: 20
Enter the 2nd x coordinate: -1
Enter the 2nd y coordinate: 0
The line is not vertical.
"""
"""
# Problem 3
time1 = int(input("First time: "))
suffix1 = input("suffix('am' or 'pm'): ")
time2 = int(input("Second time: "))
suffix2 = input("suffix('am' or 'pm'): ")
if time1 < time2:
    if suffix1 == 'am' and suffix2 == 'pm':
        print("Before")
    elif suffix1 == 'pm' and suffix2 == 'am':
        print("After")
    else:
        if time2 == 12:
            print("After")
        else:
            print("Before")
elif time1 > time2:
    if suffix1 == 'am' and suffix2 == 'pm':
        print("Before")
    elif suffix1 == 'pm' and suffix2 == 'am':
        print("After")
    else:
        if time1 == 12:
            print("Before")
        else:
            print("After")
else:
    if suffix1 == 'am' and suffix2 == 'pm':
        print("Before")
    elif suffix1 == 'pm' and suffix2 == 'am':
        print("After")
    else:
        print("Same")
"""
"""
# Problem 3 outputs
First time: 1
suffix('am' or 'pm'): am
Second time: 2
suffix('am' or 'pm'): pm
Before

First time: 1
suffix('am' or 'pm'): pm
Second time: 2
suffix('am' or 'pm'): am
After

First time: 1
suffix('am' or 'pm'): am
Second time: 12
suffix('am' or 'pm'): am
After

First time: 1
suffix('am' or 'pm'): pm
Second time: 11
suffix('am' or 'pm'): pm
Before

First time: 10
suffix('am' or 'pm'): am
Second time: 1
suffix('am' or 'pm'): pm
Before

First time: 10
suffix('am' or 'pm'): pm
Second time: 1
suffix('am' or 'pm'): am
After

First time: 12
suffix('am' or 'pm'): am
Second time: 1
suffix('am' or 'pm'): am
Before

First time: 10
suffix('am' or 'pm'): pm
Second time: 1
suffix('am' or 'pm'): pm
After

First time: 1
suffix('am' or 'pm'): am
Second time: 1
suffix('am' or 'pm'): pm
Before

First time: 1
suffix('am' or 'pm'): pm
Second time: 1
suffix('am' or 'pm'): am
After

First time: 12
suffix('am' or 'pm'): pm
Second time: 12
suffix('am' or 'pm'): pm
Same
"""
# Problem 4

"""
# Problem 4 outputs

"""