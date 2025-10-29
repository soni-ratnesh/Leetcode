class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = [0]*len(nums)
        r_sum = [0]*len(nums)
                
        s = 0
        for ii in range(len(nums)-1,-1,-1):
            r_sum[ii]=s
            s+=nums[ii]

        s = 0
        for ii in range(len(nums)):
            l_sum[ii]=s
            if r_sum[ii] == l_sum[ii]:
                return ii
            s+=nums[ii]

        return -1
            