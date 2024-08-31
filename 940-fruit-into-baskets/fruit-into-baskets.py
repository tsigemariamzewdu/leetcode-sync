class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count=collections.defaultdict(int)
        l=0
        total=0
        res=0

        for r in range(len(fruits)):
            count[fruits[r]] +=1
            total +=1

            while len(count)>2:
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1

                if not count[f]:
                    count.pop(f)
            res=max(res,total)
        return res

       
        
