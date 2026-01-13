class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        exists = {}

        for ii, num in enumerate(nums):
            if (num) in exists:
                return [exists[num], ii]
            exists[target-num] = ii
        