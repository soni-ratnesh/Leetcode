class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0

        curr_sum = nums[0]
        ii, jj=0,1
        while jj<len(nums) and curr_sum <target:
            curr_sum += nums[jj]
            jj+=1

        jj-=1
        result = (jj-ii+1) if jj<len(nums) and curr_sum >=target else 0
   
        while jj<len(nums):

            if result ==1:
                return result
            if curr_sum >= target:

                result = min(result, jj-ii+1)
                curr_sum -= nums[ii]
                ii+=1
                
            else:
                jj+=1
                if jj>=len(nums):
                    break
                curr_sum += nums[jj]
                


        return result