class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for _ in range(len(nums)):
            num = nums[0]

            if num == nums[num]:
                return num
            nums[num], nums[0]= nums[0], nums[num]
        return nums[0] 
            