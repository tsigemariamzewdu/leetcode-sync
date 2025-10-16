class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result=[]
        count=defaultdict(int)

        for word in words:
            for i in range(len(word)):
                count[word[:i+1]]+=1
        for word in words:
            score=0
            for i in range(len(word)):
                score+= count[word[:i+1]]
            result.append(score)
        return result

        