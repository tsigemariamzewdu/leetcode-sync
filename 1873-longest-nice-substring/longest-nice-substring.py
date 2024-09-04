class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice_substring(substring:str)->bool:
            char_set=set(substring)
            for char in substring:
                if char.swapcase() not in char_set:
                    return False
            return True
        longest_nice=""
        for start_index in range(len(s)):
            for end_index in range(start_index+1,len(s)):
                current_substring=s[start_index:end_index+1]
                if is_nice_substring(current_substring):
                    if len(current_substring)>len(longest_nice):
                        longest_nice=current_substring
        return longest_nice