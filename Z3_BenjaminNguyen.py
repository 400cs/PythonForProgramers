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
"""
# Problem 4
width = float(input("Input the width of the picture: "))
height = float(input("Input the height of the picture: "))
if width > height:
    print("Landscape")
elif height > width:
    print("Portrait")
else:
    print("Square")
"""
"""
# Problem 4 output
Input the width of the picture: 10
Input the height of the picture: 12
Portrait

Input the width of the picture: 12.0
Input the height of the picture: 10.0
Landscape

Input the width of the picture: 9
Input the height of the picture: 9
Square
"""
"""
# Problem 5
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
if num1.isdigit():
    if num2.isdigit():
        if int(num2) != 0:
            print(int(num1) % int(num2))
        else:
            print("The second number cannot be zero.")
    else:
        print("The second number is not a integer.")
else:
    print("The first number is not a integer.")
"""
"""
# Problem 5 outputs
Enter the first number: 10.2
Enter the second number: 1
The first number is not a integer.

Enter the first number: 10
Enter the second number: 2.2
The second number is not a integer.

Enter the first number: 10
Enter the second number: 0
The second number cannot be zero.

Enter the first number: 10
Enter the second number: 3
1
"""