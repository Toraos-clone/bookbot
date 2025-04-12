def get_num_words(text):
    words = text.split()
    return len(words)

def charCount(text):
    charDict = {}
    for char in text:
        char = char.lower()
        if char not in charDict.keys():
            charDict[char] = 1
        else:
            charDict[char] += 1
    return charDict