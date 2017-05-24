import re

def countWordOccurrences():
    numWords = {}
    with open('CompleteShakespeare.txt', 'r') as f:
        for line in f:
            line = re.findall(r"[\w]+|[^\s\w]", line)
            for word in line:
                if word not in numWords:
                    numWords[word] = 1
                else:
                    numWords[word] += 1
    return numWords

sortedOutput = sorted(countWordOccurrences(), key = countWordOccurrences().get, reverse = True)

top15Unigrams = sortedOutput[:15]

print top15Unigrams