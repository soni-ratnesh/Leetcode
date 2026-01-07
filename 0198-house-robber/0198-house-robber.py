class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        robbed = [0]*len(nums)
        robbed[0] = nums[0]
        robbed[1] = max(robbed[0],nums[1]) 

        for ii in range(2, len(nums)):
            robbed[ii] = max(robbed[ii-2]+nums[ii], robbed[ii-1])
        
        return robbed[-1]