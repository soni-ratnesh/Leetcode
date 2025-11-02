class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = 0
        for ii in range(k):
            r+=nums[ii]
        m = r/k
        for ii in range(k,len(nums)):
            r-=nums[ii-k]
            r+=nums[ii]
            m = max(r/k,m)
        return m
        