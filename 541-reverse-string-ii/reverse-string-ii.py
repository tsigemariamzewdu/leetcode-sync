class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        for i in range(0, len(s), 2 * k):
            
            result.append(s[i:i + k][::-1])
           
            result.append(s[i + k:i + 2 * k])
        return ''.join(result)
