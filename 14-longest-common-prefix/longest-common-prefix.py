class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]

        for s in strs[1:]:
            while s[:len(prefix)]!= prefix:
                prefix=prefix[:-1]
                if not prefix: # if the prefix is empty
                    return ""
        return prefix
        
        