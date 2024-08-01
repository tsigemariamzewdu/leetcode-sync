class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    fsum = nums[i] + nums[j] + nums[k] + nums[l]
                    if fsum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

                        # Skip duplicates for the third and fourth elements
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1

                        k += 1
                        l -= 1
                    elif fsum < target:
                        k += 1
                    else:
                        l -= 1

        return res
