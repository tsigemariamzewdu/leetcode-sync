class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[]
        value_map=defaultdict(int)

        for i in range(len(nums2)):

            while stack and  nums2[i]>stack[-1]:
                value_map[stack[-1]]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for num in nums1:
            ans.append(value_map[num]) if value_map[num]!=0 else ans.append(-1)
        return ans
        

     
        