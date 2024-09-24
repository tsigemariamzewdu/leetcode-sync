class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n
        
        if k > 0:
            newcode = code + code + code
            for i in range(n):
                result[i] = sum(newcode[n + i + 1 : n + i + 1 + k])
        elif k < 0:
            newcode = code + code
            for i in range(n):
                result[i] = sum(newcode[n + i + k : n + i])
        else:
            return result
        
        return result
