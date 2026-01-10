class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
	
        ii, jj = 0, 0
        count = 1
        while jj<len(nums):
            if nums[jj] == nums[ii]:
                jj+=1
            else:
                ii+=1
                nums[ii] = nums[jj]
                jj+=1
                count+=1
        return count
