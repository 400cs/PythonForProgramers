# Authors: Benjamin Nguyen
# Assignment: Z7 Substitute
# Completed (or last revision): 03/26/2024
"""
# Problem 1
def task1():
    rainbow_colors = {"red","orange","yellow","green","blue","indigo","violet"}
    colors_input = input("Enter the colors: ")
    colors_list = colors_input.split()
    colors_set = set()
    colors_set.update(colors_list)
    print(colors_set)
    if colors_set.issubset(rainbow_colors):
        print("The colors entered were a subset of rainbow colors.")
    else:
        print("The colors entered were not a subset of rainbow colors.")
"""
"""
# Problem 1 Output
Enter the colors: red red yellow blue yellow gold gray gold blue gray
{'gray', 'yellow', 'blue', 'red', 'gold'}
The colors entered were not a subset of rainbow colors.
Enter the colors: red blue blue red red yellow green yellow
{'blue', 'yellow', 'red', 'green'}
The colors entered were a subset of rainbow colors.
"""
"""
# Problem 2
def task2():
    fruits_input = input("Enter the fruits for basket1: ")
    set1 = set(fruits_input.split())
    fruits_input = input("Enter the fruits for basket2: ")
    set2 = set(fruits_input.split())
    fruits_input = input("Enter the fruits for basket3: ")
    set3 = set(fruits_input.split())
    new_set = set1 | set2
    new_set = new_set - set3
    print(f"The fruits that are in basket1 or basket2 but not in basket3 are {new_set}")
"""
"""
# Problem 2 Output
Enter the fruits for basket1: apple banana guava orange
Enter the fruits for basket2: apple cherry guava blueberry watermelon peach pear
Enter the fruits for basket3: banana guava honeydew melon apple
The fruits that are in basket1 or basket2 but not in basket3 are {'cherry', 'orange', 'pear', 'blueberry', 'peach', 'watermelon'}
Enter the fruits for basket1: mango lemon strawberry blueberry banana
Enter the fruits for basket2: guava cherry orange lemon apple honeydew mango
Enter the fruits for basket3: blueberry cherry banana mango
The fruits that are in basket1 or basket2 but not in basket3 are {'orange', 'guava', 'apple', 'strawberry', 'lemon', 'honeydew'}
"""
"""
# Problem 3
def task3(sentence):
    word_list = (sentence.lower()).split()
    word_count_dict = {}
    for word in word_list:
        new_word = word.strip(",.")
        if new_word in word_count_dict:
            word_count_dict[new_word] += 1
        else:
            word_count_dict[new_word] = 1
    print(word_count_dict)
"""
"""
# Problem 3 Output
{'i': 5, 'felt': 1, 'happy': 4, 'because': 2, 'saw': 1, 'the': 1, 'others': 1, 'were': 1, 'and': 1, 'knew': 1, 
 'should': 1, 'feel': 1, 'but': 1, 'wasn’t': 1, 'really': 1}
{'to': 2, 'be': 2, 'or': 1, 'not': 1}
"""
"""
# Problem 4
def task4():
    periodicTable = {
        "H": "Hydrogen", "C": "Carbon", "O": "Oxygen",
        "Fe": "Iron", "Au": "Gold", "Na": "Sodium",
        "Ag": "Silver", "Pb": "Lead", "Pu": "Plutonium"
    }
    elementSymbol = input("Enter a element symbol: ")
    if elementSymbol in periodicTable:
        print(periodicTable[elementSymbol])
    else:
        while elementSymbol not in periodicTable:
            print("That is not a valid element symbol. Try again.")
            elementSymbol = input("Enter a element symbol: ")
        else:
            print(periodicTable[elementSymbol])
"""
"""
# Problem 4 Output
Enter a element symbol: Fe
Iron
Enter a element symbol: C
Carbon
Enter a element symbol: H
Hydrogen
Enter a element symbol: Ne
That is not a valid element symbol. Try again.
Enter a element symbol: Na
Sodium
"""

def main():
    for _ in range(2):
        task1()
    for _ in range(2):
        task2()
    task3("I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy.")
    task3("To be, or not to be")
    for _ in range(4):
        task4()

main()
