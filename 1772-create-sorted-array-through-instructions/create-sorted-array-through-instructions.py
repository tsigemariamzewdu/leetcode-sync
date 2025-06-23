class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n=len(instructions)
        nums=[(val,i) for i,val in enumerate(instructions)]
        less=[0]*n
        great=[0]*n

        def merge_sort_greater(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=merge_sort_greater(arr[:mid])
            right=merge_sort_greater(arr[mid:])

            merged=[]
            i=0
            j=0

     

            while i<len(left) and j<len(right):
                if left[i][0] <=right[j][0]:
                    merged.append(left[i])
                    i+=1
                else:
                    
                    great[right[j][1]]+= len(left)-i
                  
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        def merge_sort_smaller(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=merge_sort_smaller(arr[:mid])
            right=merge_sort_smaller(arr[mid:])

            merged=[]
            i=0
            j=0
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    merged.append(left[i])
                    i += 1
                else:
                    less[right[j][1]] += i
                    merged.append(right[j])
                    j += 1
            
            while j < len(right):
                less[right[j][1]] += len(left)
                merged.append(right[j])
                j += 1
            merged.extend(left[i:])
            return merged



        merge_sort_smaller(nums)
        merge_sort_greater(nums)
        result=0
        for i in range(n):
            result += min(less[i],great[i])

            result %= 10**9 + 7
        return result
        