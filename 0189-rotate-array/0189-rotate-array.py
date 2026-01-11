class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse
        for ii in range(len(nums)//2):
            nums[ii], nums[len(nums)-ii-1] =  nums[len(nums)-ii-1], nums[ii]

        k = k%len(nums)
        # reverse first k
        ii, jj = 0, k-1
        while ii<jj:
            nums[ii], nums[jj] = nums[jj], nums[ii]
            ii+=1
            jj-=1
        
        ii, jj = k, len(nums)-1
        while ii<jj:
            nums[ii], nums[jj] = nums[jj], nums[ii]
            ii+=1
            jj-=1