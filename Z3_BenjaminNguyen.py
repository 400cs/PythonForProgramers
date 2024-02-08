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