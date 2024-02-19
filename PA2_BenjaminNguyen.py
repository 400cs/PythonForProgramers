# Authors: Benjamin Nguyen
# Assignment:  Programming Assignment #2
# Completed (or last revision): 02/24/2024
import math
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
# Task 1 output
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
# Task 2
#def task2():


# Task 3
#def task3():


"""
def main():
    task1()
    task2()
    task3()
if __name__ == '__main__':
    main()      # call main to run
"""