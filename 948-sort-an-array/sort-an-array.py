class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half) -> List[int]:
            
            left, right = 0, 0
            merged = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1
            
            while left < len(left_half):
                merged.append(left_half[left])
                left += 1
                
            while right < len(right_half):
                merged.append(right_half[right])
                right += 1
            
            return merged

        def mergeSort(arr):
            mid=len(arr)//2
            if len(arr) == 1:
                return arr
            rightarr=mergeSort(arr[mid:])
            leftarr=mergeSort(arr[:mid])


            return merge(leftarr, rightarr)
        return mergeSort(nums)
         

