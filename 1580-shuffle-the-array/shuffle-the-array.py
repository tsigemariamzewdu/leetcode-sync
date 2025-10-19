class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        j=n
        i=0

        while j<len(nums):
            result.append(nums[i])
            result.append(nums[j])
            i+=1
            j+=1
        return result
        