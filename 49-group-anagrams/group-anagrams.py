from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
         
        for word in strs:
            sortedword=''.join(sorted(word))
            anagrams[sortedword].append(word)
        return list(anagrams.values())
        
        

        