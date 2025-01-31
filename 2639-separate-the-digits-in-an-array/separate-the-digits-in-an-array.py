class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            i=str(i)
            for j in i:
                result.append(int(j))
        return result


       



        