class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num]=count.get(num,0)+1

        result=[]
        for num in arr2:
            if num in count:
                result.extend([num]*count[num])
                # after adding the element delete
                del count[num]
        # now add the rest in ascending order 
        remaining = []
        for num in count:
            for _ in range(count[num]):  # Add each number count[num] times
                remaining.append(num)
        remaining.sort()  # Sort the list in ascending order

        result.extend(remaining)
        return result

    