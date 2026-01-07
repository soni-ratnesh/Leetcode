class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 10**6

        ii, jj = 0,0
        curr_sum = 0
        while jj<len(nums):
            curr_sum += nums[jj]
            jj+=1
            while curr_sum>=target:
                result = min(result, jj-ii)
                curr_sum-=nums[ii]
                ii+=1
           
            

        return result if result!=10**6 else 0            