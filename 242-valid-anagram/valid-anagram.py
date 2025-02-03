class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        for j in t:
            if j in dict_s:
                dict_s[j] -= 1
            else:
                return False
        for value in dict_s.values():
            if value != 0:
                return False
        return True