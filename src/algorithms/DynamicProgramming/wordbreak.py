


def wordBreak(wordList, word): 
    if word == '': 
        return True
    else: 
        wordLen = len(word) 
        return any([(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]) 


s = "ilikeanurag"
arr = ["anurag", "sarkar", "saurav", "i", "like", "icecream"]

print(wordBreak(arr, s))