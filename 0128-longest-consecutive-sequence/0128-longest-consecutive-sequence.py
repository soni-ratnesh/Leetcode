class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)

        max_seq_count = 0

        for num in nums_set:
            if num-1 not in nums_set:
                curr_count = 0
                while num in nums_set:
                    num+=1
                    curr_count+=1
                max_seq_count = max(max_seq_count, curr_count)

        return max_seq_count 
