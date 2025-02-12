class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=[]
        l=0
        r=len(height)-1

        while l<r:
            mini=min(height[l],height[r])
            print(height[l])
            print(height[r])
            res.append(mini*(r-l))
            if mini==height[l]:
                l+=1
            else:
                r-=1
        return max(res)

        

        

        
        
        