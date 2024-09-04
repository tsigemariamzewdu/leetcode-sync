class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # this asks us to use sliding window 
        vowel='aeiou'
        def vowelCounter(substring):
            count=0
            for i in substring:
                if i in vowel:
                    count +=1
            return count

        n=len(s)
        substring=s[:k]
        currentvowel=vowelCounter(substring)
        maxvowel=currentvowel

        for i in range(1, n - k + 1):
            # Remove the influence of the character that's sliding out and add the character sliding in
            if s[i - 1] in vowel:
                currentvowel -= 1
            if s[i + k - 1] in vowel:
               currentvowel += 1
            maxvowel=max(maxvowel,currentvowel)
        
            
        return maxvowel

        