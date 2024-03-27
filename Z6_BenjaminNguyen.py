# Authors: Benjamin Nguyen
# Assignment: Z6 Substitute
# Completed (or last revision): 03/19/2024
import random
"""
# Problem 1
def task1():
    def doublinglist(list):
        listDouble = []
        for i in list:
            listDouble.append(i * 2)
        return list, listDouble

    list = [2, 3, 5, 7, 11, 13, 17]
    list2 = ["hello", "bye", "happy", "good", "excellent", "fun"]
    print(doublinglist(list))
    print(doublinglist(list2))
"""
"""
# Problem 1 Output
([2, 3, 5, 7, 11, 13, 17], [4, 6, 10, 14, 22, 26, 34])
(['hello', 'bye', 'happy', 'good', 'excellent', 'fun'], ['hellohello', 'byebye', 'happyhappy', 'goodgood', 'excellentexcellent', 'funfun'])
"""
"""
# Problem 2
def task2():
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = int(input("Enter the month (1 for January, 2 for February, and so on): "))
    if 1 <= month <= 12:
        num_days = daysInMonth[month - 1]
        print(f"Number of days in month {month} is: {num_days}")
    else:
        print("Invalid input. Month must be between 1 and 12.")
"""
"""
# Problem 2 Output
Enter the month (1 for January, 2 for February, and so on): 1
Number of days in month 1 is: 31
Enter the month (1 for January, 2 for February, and so on): 2
Number of days in month 2 is: 28
Enter the month (1 for January, 2 for February, and so on): 3
Number of days in month 3 is: 31
"""
"""
# Problem 3
def task3():
    def wordsOfLength(words, wordLength):
        wordLength_list = []
        for word in words:
            if len(word) == wordLength:
                wordLength_list.append(word)
        return wordLength_list

    words = ["hello", "bye", "happy", "good", "excellent", "fun"]
    print(wordsOfLength(words, 5))
    print(wordsOfLength(words, 7))
    words2 = ["hi", "by", "ok", "YO", "hello", "bye", "happy", "good", "excellent", "fun"]
    print(wordsOfLength(words2, 2))
"""
"""
# Problem 3 Output
['hello', 'happy']
[]
['hi', 'by', 'ok', 'YO']
"""
"""
# Problem 4
def task4(list_len):
    def removeOdd(list):
        i = 0
        while i < len(list):
            if list[i] % 2 != 0:
                list.pop(i)
            else:
                i += 1
        return list

    random_list = [random.randint(0, 99) for _ in range(list_len)]
    print("Original list:", random_list)
    print("List after removing odd values:", removeOdd(random_list))
"""
"""
# Problem 4 Output
Original list: [79, 48, 27, 20, 8, 49, 59, 74, 88, 51]
List after removing odd values: [48, 20, 8, 74, 88]
Original list: []
List after removing odd values: []
Original list: [49, 89, 64, 19, 37, 15, 17, 5, 87, 81, 81, 31, 78, 10, 61, 97, 27, 30, 41, 56, 58, 57, 92, 91, 13]
List after removing odd values: [64, 78, 10, 30, 56, 58, 92]
"""
"""
# Problem 5
def task5():
    def find_next(lst, current_pos, value_to_be_found):
        i = current_pos
        while i < len(lst):
            if lst[i] == value_to_be_found:
                return i
            i += 1

    list = [20, 30, 22, 15, 432, 45, 30, 40, 45, 30, 40]
    list2 = ["hello", "bye", "happy", "good", "happy", "fun", "hello", "Hello", "excellent", "fun"]
    print("The next occurrence is at", find_next(list, 2, 30))
    print("The next occurrence is at", find_next(list2, 5, "fun"))
    print("The next occurrence is at", find_next(list2, 6, "hello"))
"""
"""
# Problem 5 Output
The next occurrence is at 6
The next occurrence is at 5
The next occurrence is at 6
"""
def main():
    task1()
    for _ in range(3):
        task2()
    task3()
    task4(10)
    task4(0)
    task4(25)
    task5()
main()