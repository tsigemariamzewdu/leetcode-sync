class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            middle_num=num//3
            return [middle_num-1,middle_num,middle_num+1]
        return []
        