class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = {}
        for i in s:
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        for j in t:
            if j in hash_s:
                hash_s[j] -= 1
            else:
                return False
        for value in hash_s.values():
            if value != 0:
                return False
        return True
        