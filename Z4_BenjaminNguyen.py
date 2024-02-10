# Authors: Benjamin Nguyen
# Assignment: Z4 Substitute
# Completed (or last revision): 02/10/2024
"""
# Problem 1
a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))
n = int(input("Enter the number for n: "))
count = 0
for i in range(a, b + 1):
    if i % n == 0:
        count += 1
print("count: %d" % count)
"""
"""
# Problem 1 output
Enter the number for a: 2
Enter the number for b: 10
Enter the number for n: 2
count: 5

Enter the number for a: 1
Enter the number for b: 20
Enter the number for n: 1
count: 20
"""
"""
# Problem 2
n = int(input("Enter the number for n: "))
for i in range(1, n + 1):
    print("-" * (n - i) + "*" * (2 * i - 1) + "-" * (n - i))

for i in range(n - 1, 0, -1):
    print("-" * (n - i) + "*" * (2 * i - 1) + "-" * (n - i))
"""
"""
# Problem 2 output
Enter the number for n: 3
--*--
-***-
*****
-***-
--*--

Enter the number for n: 5
----*----
---***---
--*****--
-*******-
*********
-*******-
--*****--
---***---
----*----
"""
"""
# Problem 3
word = input("Enter an English word: ")
found = False
position = len(word) - 1
while not found and position >= 0:
    ch = word[position]
    if ch.isupper():
        found = True
    else:
        position -= 1
print("Position of the last uppercase letter:", position)
"""
"""
# Problem 3 output
Enter an English word: BoB
Position of the last uppercase letter: 2

Enter an English word: bob
Position of the last uppercase letter: -1
"""