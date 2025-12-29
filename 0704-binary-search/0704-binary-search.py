class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ii, jj = 0, len(nums)-1
        while ii<=jj:
            mid = (ii+jj)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                jj = mid-1
            else:
                ii = mid+1
        return -1