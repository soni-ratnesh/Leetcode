class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_pointer = 0

        for ii in range(len(nums)):
            if nums[ii] != 0:
                nums[num_pointer] = nums[ii]
                num_pointer +=1

        for ii in range(num_pointer, len(nums)):
            nums[ii] = 0