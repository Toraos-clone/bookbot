def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    numWords = getNumWords(text)
    charCounts = charCount(text)
    print(f"--- Begin report of {bookPath} ---")
    print(f"There were {numWords} words found in the document")
    #print(charCount)
    printOrderedChars(charCounts)
    print("--- End report ---")
    

def getNumWords(text):
    words = text.split()
    return len(words)


def getBookText(path):
    with open(path) as f:
        return f.read()
    

def charCount(text):
    charDict = {}
    for char in text:
        char = char.lower()
        if char not in charDict.keys():
            charDict[char] = 1
        else:
            charDict[char] += 1
    return charDict
    
def printOrderedChars(charCounts):
    def getCount(item):
        return item[1]
    sortedChars = sorted(charCounts.items(), key=getCount, reverse=True)
    for char, count in sortedChars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
        
main()
