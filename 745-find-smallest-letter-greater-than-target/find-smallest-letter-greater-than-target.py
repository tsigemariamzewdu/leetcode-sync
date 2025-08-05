class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1

        while low<=high:
            mid=(low+high)//2
            print(mid)

            if letters[mid]>target:
                high=mid-1
            else:
                low=mid+1
        if low>=len(letters):
            low=0
        return letters[low]
        
        