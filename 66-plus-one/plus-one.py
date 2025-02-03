class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit=""
        for i in digits:
            digit += str(i)
        newarr=int(digit)+1
        result=[]
        for i in str(newarr):
            result.append(int(i))
        return result

        