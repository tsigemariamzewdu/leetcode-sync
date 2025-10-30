class Solution:
    def countVowels(self, word: str) -> int:
        vowels=set(["a","e","i","o","u"])
        res=0
        for i in range(len(word)):
            if word[i] in vowels:
                res += (i+1)*(len(word)-i)
        return res
        