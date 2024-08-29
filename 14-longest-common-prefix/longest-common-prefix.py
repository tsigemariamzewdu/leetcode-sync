class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # edge case
        if not strs:
            return ""
        prefix=strs[0]

        for s in strs[1:]:
            while s[:len(prefix)]!= prefix:
                prefix=prefix[:-1]
                if not prefix: # if the prefix is empty
                    return ""
        return prefix
        

