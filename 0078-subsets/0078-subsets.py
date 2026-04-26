class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [s + [num] for s in result]
        return result