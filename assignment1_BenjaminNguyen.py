# Authors: Benjamin Nguyen
# Assignment: Programming Assignment 1
# Completed (or last revision): 02/08/2024
"""
# Task 1: Practice arithmetic expressions
PV = float(input("Enter the present dollar amount (float): "))
INT = float(input("Enter the interest rate (float): "))
YRS = int(input("Enter the number of years (integer): "))
print("The future value is $%.2f" % (PV * (1 + INT / 100) ** YRS))

# tests' outputs
Enter the present dollar amount (float): 1000.0
Enter the interest rate (float): 5.0
Enter the number of years (integer): 30
The future value is $4321.94
Enter the present dollar amount (float): 1530.50
Enter the interest rate (float): 3.5
Enter the number of years (integer): 15
The future value is $2564.12
Enter the present dollar amount (float): 100.0
Enter the interest rate (float): 1.0
Enter the number of years (integer): 10
The future value is $110.46
"""
"""
# Task 2: Practice assignments
num1 = int(input("Enter a number (integer): "))
num2 = int(input("Enter a number (integer): "))
print("Before the swap, the first number was", num1, ",and the second number was", num2)
num1, num2 = num2, num1
print("After the swap, the first number is", num1, ",and the second number is", num2)

# tests' outputs
Enter a number (integer): 7
Enter a number (integer): 9
Before the swap, the first number was 7 ,and the second number was 9
After the swap, the first number is 9 ,and the second number is 7
Enter a number (integer): 10
Enter a number (integer): 1
Before the swap, the first number was 10 ,and the second number was 1
After the swap, the first number is 1 ,and the second number is 10
"""
