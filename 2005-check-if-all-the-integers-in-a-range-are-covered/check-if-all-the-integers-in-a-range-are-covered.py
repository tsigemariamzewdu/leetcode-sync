class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        k=0
        for i in range(left,right+1):
            flag=False
            for s,e in ranges:
                if s<=i<=e:
                    flag=True
                    break
               
            if not flag:
                return False
        return True
        




        