class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        # Convert the string to a list of characters
        s_list = list(s)
        
        # Two pointers
        l = 0
        r = len(s_list) - 1
        
        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowels:
                r -= 1
            elif s_list[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        
        # Convert the list of characters back to a string
        return ''.join(s_list)