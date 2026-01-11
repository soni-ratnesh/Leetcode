class Solution:
    
    def reverse(self, nums, ii, jj):
        while ii<jj:
            nums[ii], nums[jj] = nums[jj], nums[ii]
            ii+=1
            jj-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        is_reverse=True
        # first ele less than last
        for ii in range(len(nums)-1, 0, -1):
            if nums[ii-1]<nums[ii]:
                ii-=1
                is_reverse=False
                break
        
        #if i is zero reverse array
        if is_reverse:
            self.reverse(nums, 0, len(nums)-1)
        else:
            for jj in range(len(nums)-1, ii, -1):
                if nums[ii]<nums[jj]:
                    break

            nums[ii], nums[jj] = nums[jj], nums[ii]
            self.reverse(nums, ii+1, len(nums)-1)
        
        