class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_arr=[]
        counter=Counter(nums)
        r=max(nums)-min(nums)+1

        offset=min(nums)
        result=[0]*r
        for i in counter:
            result[i-offset]=counter[i]
        for i in range(len(result)):
            for _ in range(result[i]):
                sorted_arr.append(i+offset)
        return sorted_arr

        