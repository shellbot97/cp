def bruteIsAnagram(word1: str, word2: str) -> bool: 
    if len(word1) != len(word2):
        return False
    charCount = {}
    for char in word1:
        charCount[char] = charCount.get(char, 0) + 1
    for char in word2:
        if char not in charCount:
            return False
        charCount[char] -= 1
        if charCount[char] < 0:
            return False
    return True

def optimizedIsAnagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    charSet = set(word1)
    for char in charSet:
        if word1.count(char) != word2.count(char):
            return False
    return True  
    

    

if bruteIsAnagram("carrace", "racecar"):
    print("anagram")
else:
    print("not anagram")

'''

leanings:

If word1.count(char) and word2.count(char) are O(n) operations each and it already runs insdie for loop, shouldn't it be O(n^3) since there are total 3 loops runnning:
n * (O(n) + O(n)) = n * 2O(n) = O(n²)
                                  
Why is  n * 2O(n) = O(n²) shouldn't it be 2O(n²)
Big-O describes the asymptotic behavior — how the algorithm scales as input grows large (n → ∞). The constant multiplier (like 2 or 1000) doesn’t affect the growth rate.
'''