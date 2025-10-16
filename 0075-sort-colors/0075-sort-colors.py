class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter ={}

        for num in nums:
            counter[num] = counter.get(num,0)+1
        
        for ii in range(len(nums)):
            if counter.get(0,0):
                nums[ii] = 0
                counter[0] -= 1
                continue
            elif counter.get(1,0):
                nums[ii] = 1
                counter[1] -= 1
                continue
            elif counter.get(2,0):
                nums[ii] = 2
                counter[2] -= 1
                continue
