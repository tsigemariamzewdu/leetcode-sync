class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left=0 
        right=len(height)-1
        while left<right:
            width=right-left
            area_= width*min(height[left],height[right])
            max_area=max(max_area,area_)
            if height[left]<height[right]:
                left +=1
            else:
                right-=1
        return max_area

        

        
        
        