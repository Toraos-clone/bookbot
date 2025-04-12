from stats import get_num_words
from stats import charCount
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = sys.argv[1]
    text = getBookText(bookPath)
    numWords = get_num_words(text)
    charCounts = charCount(text)
    print("--- Begin report of Frankenstein; Or, The Modern Prometheus ---")
    print(f"Found {numWords} total words")
    #print(charCount)
    printOrderedChars(charCounts)
    print("--- End report ---")
    

# def getNumWords(text):
#     words = text.split()
#     return len(words)


def getBookText(path):
    with open(path) as f:
        return f.read()
    

# def charCount(text):
#     charDict = {}
#     for char in text:
#         char = char.lower()
#         if char not in charDict.keys():
#             charDict[char] = 1
#         else:
#             charDict[char] += 1
#     return charDict
    
def printOrderedChars(charCounts):
    def getCount(item):
        return item[1]
    sortedChars = sorted(charCounts.items(), key=getCount, reverse=True)
    for char, count in sortedChars:
        if char.isalpha():
            print(f"{char}: {count}")
        
main()
