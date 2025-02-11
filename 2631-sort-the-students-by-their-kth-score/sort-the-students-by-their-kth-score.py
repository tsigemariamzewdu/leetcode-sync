class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows=len(score)
        cols=len(score[0])
        result=[]
        realres=[]

        for r in range(rows):
            for c in range(cols):
                if c==k:
                    result.append([r,score[r][c]])
        result.sort(key=lambda list: list[1],reverse=True)
        res=[]
        for i in result:
            res.append(i[0])
        for j in range(len(score)):
            realres.append(score[res[j]])
        return realres

        

        