class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        def binary_search(arr,x):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        
        # we are supposed to use a binary search
        arr2.sort()
        count =0
        for a in arr1:
            position=binary_search(arr2,a)

            if (position == 0 or abs(a - arr2[position - 1]) > d) and (position == len(arr2) or abs(a - arr2[position]) > d):
                count += 1
        return count
        