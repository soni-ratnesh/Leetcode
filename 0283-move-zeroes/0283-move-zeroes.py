class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ii, jj = 0,0

        while jj<len(nums):
            if nums[jj]!=0:
                nums[ii], nums[jj] = nums[jj], nums[ii]
                ii+=1
            jj+=1
