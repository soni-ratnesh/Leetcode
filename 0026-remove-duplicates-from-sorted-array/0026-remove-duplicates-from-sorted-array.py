class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ii, jj = 0, 1
        count = 1
        while jj<len(nums):
            if nums[ii]<nums[jj]:
                count+=1
                ii+=1
                nums[ii] = nums[jj]
            jj+=1
        
        return count