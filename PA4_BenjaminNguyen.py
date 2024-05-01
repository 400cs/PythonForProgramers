# Authors: Benjamin Nguyen
# Assignment: PA4
# Completed (or last revision): 04/29/2024
# Task 1: Text File Processing and Exception Handling
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 6. (Bonus, 5 pts) Draw a word cloud based on the word count frequency. You may use a word
# cloud generator. Note: The word cloud shown below is not related to the Python.txt text file.
# Required test runs: test run with the Python.txt and one additional text file of your choice but at least
# 20 lines long.
def task1():
    fname = input("Enter the file name: ")
    attempts = 0
    while attempts < 3:
        try:
            rfile = open(fname, 'r')
            break
        except FileNotFoundError:
            attempts += 1
            print("File not found. Please re-enter the file name.")
            fname = input("Enter file name: ")

    numOfLines = 0
    numOfWords = 0
    setOfWords = set()
    dictOfWords = {}
    for line in rfile:
        numOfLines += 1
        words = [word.strip(",.!?:;") for word in line.split()]
        i = 0
        while i < len(words):
            if words[i].isalpha():
                numOfWords += 1
                words[i] = words[i].lower()
                if words[i] in dictOfWords:
                    dictOfWords[words[i]] += 1
                else:
                    dictOfWords[words[i]] = 1
                i += 1
            else:
                words.pop(i)
        setOfWords.update(words)
    print(f"{fname} - The total number of lines are {numOfLines}, and the total number of words are {numOfWords}")
    sorted_dictOfWords = dict(sorted(dictOfWords.items(), key=lambda x:x[1], reverse=True))
    print(sorted_dictOfWords)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(sorted_dictOfWords)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    plt.close()

# Task 2: Operator Overloading (15 Points)
# (1) Define a Pair class that consists of two elements (i.e. a Pair object has two members x, y) and a
# number of methods described in (2) – (4).
# (2) Define a constructor that creates a Pair object. The default value for x and y is 0;
# (3) Define a __str__ method, so if p is a Pair object, print(p) will display in the form of <x, y>;
# (4) Use operator overloading to define the +, *, and / operators. These operators are defined as
# follows -- assume p1 = Pair(x1, y1), p2 = Pair(x2, y2)
# p1 + p2 => <x1 + x2, y1+y2> #here => means “defined as”
# p1 * p2 => <x1*x2, y1*y2>
# p1 / p2 => <x1*y1-x2*y2, x1*x2 – y1*y2>
def main():
    task1()
    task1()

main()
# Task 1 Output
"""
Enter the file name: Python.txt
Python.txt - The total number of lines are 12, and the total number of words are 128
{'the': 9, 'machine': 6, 'learning': 6, 'python': 5, 'is': 5, 'a': 5, 'of': 5, 'to': 5, 'learn': 4, 'and': 4, 'computer': 3, 'programming': 2, 'that': 2, 'from': 2, 'data': 2, 'into': 2, 'high': 1, 'level': 1, 'general': 1, 'purpose': 1, 'language': 1, 'design': 1, 'philosophy': 1, 'emphasizes': 1, 'code': 1, 'readability': 1, 'consistently': 1, 'ranks': 1, 'as': 1, 'one': 1, 'most': 1, 'popular': 1, 'languages': 1, 'field': 1, 'science': 1, 'uses': 1, 'statistical': 1, 'techniques': 1, 'give': 1, 'programs': 1, 'ability': 1, 'past': 1, 'experiences': 1, 'improve': 1, 'how': 1, 'they': 1, 'perform': 1, 'specific': 1, 'tasks': 1, 'you': 1, 'will': 1, 'steps': 1, 'necessary': 1, 'create': 1, 'successful': 1, 'application': 1, 'with': 1, 'scikit': 1, 'library': 1, 'making': 1, 'studying': 1, 'statistics': 1, 'step': 1, 'direction': 1, 'artificial': 1, 'intelligence': 1, 'program': 1, 'analyses': 1, 'learns': 1, 'predict': 1, 'outcome': 1, 'get': 1, 'ready': 1, 'dive': 1, 'world': 1, 'by': 1, 'using': 1}
Enter the file name: Python2.txt
Python2.txt - The total number of lines are 21, and the total number of words are 125
{'thy': 8, 'the': 7, 'to': 4, 'and': 4, 'by': 3, 'that': 2, 'might': 2, 'but': 2, 'his': 2, 'tender': 2, 'thou': 2, 'thine': 2, 'own': 2, 'self': 2, 'now': 2, 'in': 2, 'sonnets': 1, 'william': 1, 'shakespeare': 1, 'from': 1, 'fairest': 1, 'creatures': 1, 'we': 1, 'desire': 1, 'increase': 1, 'thereby': 1, 'rose': 1, 'never': 1, 'die': 1, 'as': 1, 'riper': 1, 'should': 1, 'time': 1, 'decease': 1, 'heir': 1, 'bear': 1, 'memory': 1, 'contracted': 1, 'bright': 1, 'eyes': 1, 'flame': 1, 'with': 1, 'fuel': 1, 'making': 1, 'a': 1, 'famine': 1, 'where': 1, 'abundance': 1, 'lies': 1, 'foe': 1, 'sweet': 1, 'too': 1, 'cruel': 1, 'art': 1, 'fresh': 1, 'ornament': 1, 'only': 1, 'herald': 1, 'gaudy': 1, 'spring': 1, 'within': 1, 'bud': 1, 'buriest': 1, 'content': 1, 'churl': 1, 'waste': 1, 'niggarding': 1, 'pity': 1, 'world': 1, 'or': 1, 'else': 1, 'this': 1, 'glutton': 1, 'be': 1, 'eat': 1, 'due': 1, 'grave': 1, 'thee': 1, 'when': 1, 'forty': 1, 'winters': 1, 'shall': 1, 'besiege': 1, 'brow': 1, 'dig': 1, 'deep': 1, 'trenches': 1, 'field': 1, 'proud': 1, 'livery': 1, 'so': 1, 'gazed': 1, 'on': 1}
"""