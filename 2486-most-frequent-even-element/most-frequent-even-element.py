class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = [num for num in nums if num % 2 == 0]
        evendict = {}
        for num in even:
            if num in evendict:
                evendict[num] += 1
            else:
                evendict[num] = 1
        
        max_count = 0
        most_frequent_even = -1
        for num, count in evendict.items():
            if count > max_count or (count == max_count and num < most_frequent_even):
                max_count = count
                most_frequent_even = num
        
        return most_frequent_even if max_count > 0 else -1