from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        # because the form that we are supposed to return is a list of list it is better to have the words appended on a list and then after creating this dictionary 
        for word in strs:
            sortedword=''.join(sorted(word))
            anagrams[sortedword].append(word)
        return list(anagrams.values())
        
        

        