class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD= (10 **9)+7
        right=0
        left=0
        rem=0
        if startPos > endPos:
            left=startPos-endPos
            if left>k:
                return 0
            rem=k-left
            if rem%2!=0:
                return 0

        else:
            right=endPos-startPos
            rem=k-right
            if rem%2!=0 or right >k:
                return 0

        right+= rem//2
        left+=rem//2
        # print(right,left,rem)

        result= math.factorial(k) // (math.factorial(right) *math.factorial(left))
        return result %MOD
        
       
        