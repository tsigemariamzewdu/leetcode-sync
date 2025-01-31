class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings=s.split()
        return len(strings[-1])
        