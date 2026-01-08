from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        n, m = len(nums1), len(nums2)

        def dp(i, j):
         
            if i == n or j == m:
                return float('-inf')

            if (i, j) in memo:
                return memo[(i, j)]

           
            take = nums1[i] * nums2[j]
            take += max(0, dp(i + 1, j + 1))

           
            skip1 = dp(i + 1, j)
            skip2 = dp(i, j + 1)

            memo[(i, j)] = max(take, skip1, skip2)
            return memo[(i, j)]

        return dp(0, 0)
