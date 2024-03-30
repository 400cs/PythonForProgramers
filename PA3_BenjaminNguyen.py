# Authors: Benjamin Nguyen
# Assignment: PA3
# Completed (or last revision): 03/29/2024
import random
import sympy
# Task 1: Password Management System
def task1():
    def authenticate(loginInfo):
        username = input("Enter your username: ")
        if username in loginInfo:
            password = input("Enter your password: ")
            if loginInfo[username] == password:
                return username
            else:
                numOfPWTries = 0
                while numOfPWTries < 3:
                    password = input("Please try entering your password again: ")
                    if loginInfo[username] == password:
                        return username
                    numOfPWTries += 1
                else:
                    return False
        else:
            numOfAttempts = 0
            while numOfAttempts < 3:
                username = input("Please try entering your username again: ")
                if username in loginInfo:
                    password = input("Enter your password: ")
                    if loginInfo[username] == password:
                        return username
                    else:
                        numOfPWTries = 0
                        while numOfPWTries < 3:
                            password = input("Please try entering your password again: ")
                            if loginInfo[username] == password:
                                return username
                            numOfPWTries += 1
                        else:
                            return False
                numOfAttempts += 1
            else:
                return False

    def create_user(loginInfo):
        new_username = input("Enter a username: ")
        contain_letters = False
        for char in new_username:
            if char.isalpha():
                contain_letters = True
                break
        if contain_letters and new_username not in loginInfo:
            new_password = input("Enter a password: ")
            at_least_8_char = False
            contain_lowercase = False
            contain_uppercase = False
            contain_digit = False
            contain_special_char = False
            if len(new_password) >= 8:
                at_least_8_char = True
            else:
                print("Invalid password entered. The length must be at least 8 characters.")
                return None
            for char in new_password:
                if char.islower():
                    contain_lowercase = True
                if char.isupper():
                    contain_uppercase = True
                if char.isdigit():
                    contain_digit = True
                if not char.isalnum() and not char.isspace():
                    contain_special_char = True
            if at_least_8_char and contain_lowercase and contain_uppercase and contain_digit and contain_special_char:
                loginInfo[new_username] = new_password
                return new_username
            else:
                print("Invalid password entered.")
                return None
        else:
            print("Invalid username entered.")
            return None

    def update_password(loginInfo, username):
        print(f"User: {username} ", end="")
        current_password = input("Enter your password: ")
        new_password = input("Enter the new password: ")
        if loginInfo[username] == current_password:
            at_least_8_char = False
            contain_lowercase = False
            contain_uppercase = False
            contain_digit = False
            contain_special_char = False
            if len(new_password) >= 8:
                at_least_8_char = True
            else:
                print("Invalid password entered. The length must be at least 8 characters.")
                return False
            for char in new_password:
                if char.islower():
                    contain_lowercase = True
                if char.isupper():
                    contain_uppercase = True
                if char.isdigit():
                    contain_digit = True
                if not char.isalnum() and not char.isspace():
                    contain_special_char = True
            if at_least_8_char and contain_lowercase and contain_uppercase and contain_digit and contain_special_char:
                loginInfo[username] = new_password
                return True
            else:
                print("Invalid password entered. The password entered does not meet the format requirements.")
                return False
        else:
            print("Invalid password entered. The password entered does not match the current password.")
            return False

    # Test Run 1
    usernames = ("lyang", "kSimon", "danny", "tomatcpp", "csDept", "CoScpp", "broncoWins", "ponyExp",
                 "BldgAndRooms", "helloKitty")
    passwords = ["sheCodes#123", "catchAllGood1%", "@my2Choices", "123abc;;;", "Hello2Monday$","GoodFriday@Cpp2",
                "CS2520@Python", "JavaIsHot2!", "2ManyRainingDays!", "1Startup@Starbucks"]
    login_dict = {usernames: passwords for usernames, passwords in zip(usernames, passwords)}
    authenticate(login_dict)
    print()
    create_user(login_dict)
    print()
    update_password(login_dict, "lyang")
    print()

    authenticate(login_dict)
    print()
    create_user(login_dict)
    print()
    update_password(login_dict, "kSimon")
    print()

    # Test Run 2
    usernames = ("Pyang", "zSimon1", "ranny", "Jimngu", "BigBucks", "Jyang", "ffsSimon", "Baus",
                 "Benngu", "Bigluck", "Bob", "JoeRogan")
    passwords = ["sheCodes#123", "catchAllGood1%", "@my2Choices", "bigCHILL!57", "Easymoney$9",
                 "Alittle#0", "NOdinos16#", "heCodes420&", "Bingbon@321", "Classic!77", "canTouch5!", "2Bigbears!"]
    login_dict = {usernames: passwords for usernames, passwords in zip(usernames, passwords)}
    authenticate(login_dict)
    print()
    create_user(login_dict)
    print()
    update_password(login_dict, "JoeRogan")
    print()

    authenticate(login_dict)
    print()
    create_user(login_dict)
    print()
    update_password(login_dict, "Bob")
    print()

# Task 2: Sets and Lists
def task2():
    for _ in range(2):
        L1 = [x for x in range(2, 500) if sympy.isprime(x)][:50]
        L2 = [random.randint(0, 100) for _ in range(50)]
        S1 = set(L1)
        S2 = set(L2)
        print("The number of elements in S1:", len(S1))
        print("The number of elements in S2:", len(S2))
        R1 = S1 & S2
        print("The number of elements in R1:", len(R1))
        R2 = (S1 | S2) - R1
        print("The number of elements in R2:", len(R2))
        print()

# Task 3: Tuples
def task3():
    def tryTuple(*args):
        minium = min(args)
        maximum = max(args)
        length = len(args)
        return minium, maximum, length

    result = tryTuple(3, 5, 12, 9, 1, 2)
    print(result)
    result = tryTuple("hi", "bye", "happy")
    print(result)
    result = tryTuple(["cat", 3], ["dog", 2])
    print(result)

def main():
    task1()
    task2()
    task3()

main()
"""
# Task 1: Test Run 1
Enter your username: lyang
Enter your password: sheCodes#123

Enter a username: Joe
Enter a password: Ilovebears@420

User: lyang Enter your password: sheCodes#123
Enter the new password: Idonotcode#123

Enter your username: asdgq
Please try entering your username again: gasdf
Please try entering your username again: fsad
Please try entering your username again: tomatcpp
Enter your password: ssdfkljjj@31
Please try entering your password again: kashdf@
Please try entering your password again: fgdfg$11
Please try entering your password again: sdafkj#44

Enter a username: byebye
Enter a password: asd
Invalid password entered. The length must be at least 8 characters.

User: kSimon Enter your password: catchAllGood1%
Enter the new password: abcabcabc1
Invalid password entered. The password entered does not meet the format requirements.

# Task 1: Test Run 2
Enter your username: 2Bigbears!
Please try entering your username again: JoeRogan
Enter your password: kdfi!234
Please try entering your password again: 2Bigbears!

Enter a username: Hey
Enter a password: YoYoYoo$;
Invalid password entered.

User: JoeRogan Enter your password: 2Bigbears!
Enter the new password: 3bearss
Invalid password entered. The length must be at least 8 characters.

Enter your username: trollolol
Please try entering your username again: bybeybe
Please try entering your username again: ohnono
Please try entering your username again: YesYes

Enter a username: 123456789
Invalid username entered.

User: Bob Enter your password: can
Enter the new password: Icandoit@45
Invalid password entered. The password entered does not match the current password.

# Task 2: Test Run 1
The number of elements in S1: 50
The number of elements in S2: 40
The number of elements in R1: 8
The number of elements in R2: 74

# Task 2: Test Run 2
The number of elements in S1: 50
The number of elements in S2: 39
The number of elements in R1: 9
The number of elements in R2: 71

# Task 3 Output
(1, 12, 6)
('bye', 'hi', 3)
(['cat', 3], ['dog', 2], 2)
"""