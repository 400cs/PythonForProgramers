# Authors: Benjamin Nguyen
# Assignment: PA3
# Completed (or last revision): 04/08/2024
import random
# Problem 1
def task1():
    file_name = input("Enter the output file name: ")
    try:
        outfile = open(file_name, "w")
        for i in range(1, 51):
            num = random.randint(-50, 50)
            outfile.write(f"A{i}: {num}\n")
        outfile.close()
    except IOError:
        print("Error with writing to file")

    try:
        negative_count = 0
        infile = open(file_name, "r")
        for line in infile:
            num = int(line.split(": ")[1])
            if num < 0:
                negative_count += 1
        print("Total number of negative values:", negative_count)
        infile.close()
    except IOError:
        print("Error with reading from file")

# Problem 2
def task2():
    print("Enter an expression or 'Stop' to exit:")
    expression = input()
    while expression != "Stop":
        parts = expression.split()
        num1_str = parts[0]
        operator = parts[1]
        num2_str = parts[2]
        try:
            try:
                num1 = float(num1_str)
            except ValueError:
                raise ValueError(f"Invalid number encountered: {num1_str}")

            try:
                num2 = float(num2_str)
            except ValueError:
                raise ValueError(f"Invalid number encountered: {num2_str}")

            if operator not in ["+", "-", "*", "/"]:
                raise ValueError(f"Invalid operator: {operator}")

            if operator == "/" and num2 == 0:
                raise ValueError("Divisor cannot be 0")

            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                print(num1 / num2)

        except ValueError as e:
            print(e)

        expression = input()

def main():
    task1()
    task2()

main()

"""
# Problem 1 Output
Enter the output file name: file.txt
Total number of negative values: 26

# Problem 2 Output
Enter an expression or 'Stop' to exit:
3 + 4
7.0
4 - 10
-6.0
3.5.2 + 3
Invalid number encountered: 3.5.2
7 * 11
77.0
7 / 2
3.5
7 // 2
Invalid operator: //
7 / 0
Divisor cannot be 0
6 * 4#2
Invalid number encountered: 4#2
2 @ 55
Invalid operator: @
0 / 2
0.0
Stop
"""