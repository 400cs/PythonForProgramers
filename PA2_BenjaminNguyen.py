# Authors: Benjamin Nguyen
# Assignment:  Programming Assignment #2
# Completed (or last revision): 02/24/2024
import math
from sympy import isprime
import time
"""
# Task 1
def task1():
    no_test = 6
    for test in range(no_test):
        print(f"Test #{test+1}:")
        x = float(input("To calculate sin(x), please enter the value of x : "))
        result = math.sin(x)
        sum = 0
        term = x
        i = 1
        while abs(sum - result) >= 0.000001:
            sum += term
            term *= (-1) * (x**2) / (2*i*(2*i+1))
            i += 1

        print(f"It takes {i} round of iterations to calculate sin({x})")
        print("Estimated result: %.6f" % sum)
        print(f"Sin({x}) from math library: {result}")
        print("Difference: %.7f" % (abs(math.sin(x) - sum)))
        print()
"""
"""
# Task 1 Output
Test #1:
To calculate sin(x), please enter the value of x : 0.0
It takes 1 round of iterations to calculate sin(0.0)
Estimated result: 0.000000
Sin(0.0) from math library: 0.0
Difference: 0.0000000

Test #2:
To calculate sin(x), please enter the value of x : 1.5709
It takes 7 round of iterations to calculate sin(1.5709)
Estimated result: 1.000000
Sin(1.5709) from math library: 0.9999999946259333
Difference: 0.0000001

Test #3:
To calculate sin(x), please enter the value of x : -3.14
It takes 9 round of iterations to calculate sin(-3.14)
Estimated result: -0.001592
Sin(-3.14) from math library: -0.0015926529164868282
Difference: 0.0000008

Test #4:
To calculate sin(x), please enter the value of x : -0.7854
It takes 5 round of iterations to calculate sin(-0.7854)
Estimated result: -0.707108
Sin(-0.7854) from math library: -0.7071080798594735
Difference: 0.0000003

Test #5:
To calculate sin(x), please enter the value of x : 2.18
It takes 8 round of iterations to calculate sin(2.18)
Estimated result: 0.820104
Sin(2.18) from math library: 0.8201039476213741
Difference: 0.0000001

Test #6:
To calculate sin(x), please enter the value of x : 3.14
It takes 9 round of iterations to calculate sin(3.14)
Estimated result: 0.001592
Sin(3.14) from math library: 0.0015926529164868282
Difference: 0.0000008
"""

"""
# Task 2
def get_input():
    str_input = input("Enter a sentence or phrase: ")
    return str_input
def get_num_of_letters(str_input):
    num_of_letter = 0
    for char in str_input:
        if char.isalpha():
            num_of_letter += 1
    return num_of_letter
def output_without_whitespace(str_input):
    non_whitespace_str = ""
    for char in str_input:
        if not char.isspace():
            non_whitespace_str += char
    return non_whitespace_str
def get_first(str_input):
    get_first_str = ""
    input_list = str_input.split()
    for word in input_list:
        get_first_str += word[0].upper()
    return get_first_str
def task2():
    for i in range(3):
        str_input = get_input()
        print(f"You entered: {str_input}")
        print(f"Total number of characters: {len(str_input)}")
        print(f"Number of letters in the sentence: {get_num_of_letters(str_input)}")
        print(f"String with no whitespace: {output_without_whitespace(str_input)}")
        print(f"First letters of words in uppercase: {get_first(str_input)}")
        print()
"""
"""
# Task 2 Output
Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.
Total number of characters: 46
Number of letters in the sentence: 36
String with no whitespace: Theonlythingwehavetofearisfearitself.
First letters of words in uppercase: TOTWHTFIFI

Enter a sentence or phrase: 		Hi, I am 9 years old.
You entered: 		Hi, I am 9 years old.
Total number of characters: 23
Number of letters in the sentence: 13
String with no whitespace: Hi,Iam9yearsold.
First letters of words in uppercase: HIA9YO

Enter a sentence or phrase: 100 plus 100 is 200!
You entered: 100 plus 100 is 200!
Total number of characters: 20
Number of letters in the sentence: 6
String with no whitespace: 100plus100is200!
First letters of words in uppercase: 1P1I2
"""

"""
# Task 3
def prime_generator():
    n = 2
    while True:
        if isprime(n):
            yield (n)
        n += 1

def task3():
    prime = prime_generator()
    for i in range(50):
        if i % 10 == 0:
            print()
        print(next(prime), end=" ")

    print('\n')
    start_time = time.time()
    print("The 101st prime number and 1100th prime number: ", end="")

    for i in range(51, 1100):
        if i == 101 or i == 1099:
            print(next(prime), end=" ")
        next(prime)
    print(f"\n{time.time() - start_time} seconds")
"""
"""
# Task 3 Output
2 3 5 7 11 13 17 19 23 29 
31 37 41 43 47 53 59 61 67 71 
73 79 83 89 97 101 103 107 109 113 
127 131 137 139 149 151 157 163 167 173 
179 181 191 193 197 199 211 223 227 229 

The 101st prime number and 1100th prime number: 547 8831 
0.0020017623901367188 seconds
"""

"""
def main():
    task1()
    task2()
    task3()
if __name__ == '__main__':
    main()      # call main to run
"""