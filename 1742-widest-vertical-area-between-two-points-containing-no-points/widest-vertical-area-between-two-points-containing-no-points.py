class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        newList=[]
        for i in points:
            newList.append(i[0])
        newList.sort()
        diff=0
        for i in range(len(newList)-1):
            difference=newList[i+1]-newList[i]
            diff=max(diff,difference)
        return diff

        