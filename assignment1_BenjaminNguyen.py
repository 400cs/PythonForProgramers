# Authors: Benjamin Nguyen
# Assignment: Programming Assignment 1
# Completed (or last revision): 02/03/2024
"""
# Task 1: Practice arithmetic expressions
PV = float(input("Enter the present dollar amount (float): $"))
INT = float(input("Enter the interest rate (float): "))
YRS = int(input("Enter the number of years (integer): "))
print("The future value is $%.2f" % (PV * (1 + INT / 100) ** YRS))
"""
"""
# Task 1 outputs
Enter the present dollar amount (float): $1000.0
Enter the interest rate (float): 5.0
Enter the number of years (integer): 30
The future value is $4321.94

Enter the present dollar amount (float): $1530.50
Enter the interest rate (float): 3.5
Enter the number of years (integer): 15
The future value is $2564.12

Enter the present dollar amount (float): $100.0
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
"""
"""
# Task 2 outputs
Enter a number (integer): 7
Enter a number (integer): 9
Before the swap, the first number was 7 ,and the second number was 9
After the swap, the first number is 9 ,and the second number is 7

Enter a number (integer): 10
Enter a number (integer): 1
Before the swap, the first number was 10 ,and the second number was 1
After the swap, the first number is 1 ,and the second number is 10
"""
"""
# Task 3: Compare and contrast
num1 = int(input("Enter the value of num1 and num2 "))
num2 = int(input())
quotient = num1 / num2
remainder = num1 % num2
print(f"Quotient when {num1}/{num2} is: {quotient}")
print(f"Remainder when {num1} is divided by {num2} is: {remainder}")
"""
r"""
# Task 3 outputs
Enter the value of num1 and num2 12
35
Quotient when 12/35 is: 0.34285714285714286
Remainder when 12 is divided by 35 is: 12

Enter the value of num1 and num2 35
13
Quotient when 35/13 is: 2.6923076923076925
Remainder when 35 is divided by 13 is: 9

Enter the value of num1 and num2 35
0
Traceback (most recent call last):
  File "C:\Users\Admin\PycharmProjects\CS2520ProgrammingAssignment1\PythonForProgrammers\assignment1_BenjaminNguyen.py",
   line 51, in <module>
    quotient = num1 / num2
               ~~~~~^~~~~~
ZeroDivisionError: division by zero
"""
"""
# Task 4: Practice if statement
measurement_system = input("Please choose a valid measurement system 'USA' or 'Metric': ")
if measurement_system == "USA":
    weight = float(input("Please enter your weight in pounds(lb): "))
    height = float(input("Please enter your height in inches(in): "))
    BMI = 703 * (weight / height ** 2)
    print("Your BMI is %.2f." % BMI)
    if BMI > 25:
        print("You are overweight.")
    elif BMI < 18:
        print("You are underweight.")
    else:
        print("You are healthy.")
elif measurement_system == "Metric":
    weight = float(input("Please enter your weight in kilograms(kg): "))
    height = float(input("Please enter your height in meters(m): "))
    BMI = weight / height ** 2
    print("Your BMI is %.2f." % BMI)
    if BMI > 25:
        print("You are overweight.")
    elif BMI < 18:
        print("You are underweight.")
    else:
        print("You are healthy.")
else:
    print("Invalid measurement system.")
"""
r"""
# Task 4 outputs
Please choose a valid measurement system 'USA' or 'Metric': USA
Please enter your weight in pounds(lb): 155
Please enter your height in inches(in): 70
Your BMI is 22.24.
You are healthy.

Please choose a valid measurement system 'USA' or 'Metric': USA
Please enter your weight in pounds(lb): 172
Please enter your height in inches(in): 68
Your BMI is 26.15.
You are overweight.

Please choose a valid measurement system 'USA' or 'Metric': Metric
Please enter your weight in kilograms(kg): 75
Please enter your height in meters(m): 1.83
Your BMI is 22.40.
You are healthy.

Please choose a valid measurement system 'USA' or 'Metric': Metric
Please enter your weight in kilograms(kg): 51.1
Please enter your height in meters(m): 1.68
Your BMI is 18.11.
You are healthy.

Please choose a valid measurement system 'USA' or 'Metric': USA
Please enter your weight in pounds(lb): 170
Please enter your height in inches(in): 67
Your BMI is 26.62.
You are overweight.

Please choose a valid measurement system 'USA' or 'Metric': Metric
Please enter your weight in kilograms(kg): 100
Please enter your height in meters(m): 1.95
Your BMI is 26.30.
You are overweight.

Please choose a valid measurement system 'USA' or 'Metric': USA
Please enter your weight in pounds(lb): -500
Please enter your height in inches(in): 50
Your BMI is -140.60.
You are underweight.

Please choose a valid measurement system 'USA' or 'Metric': USA
Please enter your weight in pounds(lb): 200
Please enter your height in inches(in): 0
Traceback (most recent call last):
  File "C:\Users\Admin\PycharmProjects\CS2520ProgrammingAssignment1\PythonForProgrammers\assignment1_BenjaminNguyen.py",
   line 82, in <module>
    BMI = 703 * (weight / height ** 2)
                 ~~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: float division by zero
"""