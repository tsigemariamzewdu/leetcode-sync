from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_chars=Counter(chars)
        count=0
        for word in words:
            count_word=Counter(word)
            cc=0
            for j in word:
                if j in count_chars:
                    if count_chars[j]>=count_word[j]:
                        cc+=1
            
            if cc==len(word):
                count+=len(word)
        return count

        