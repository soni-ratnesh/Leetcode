class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        edcaes:
        array  = []/[1]

        single pass

        """
        def count_longest(num):
            count = 0
            while num in num_set:
                count+=1
                num+=1
            return count

        num_set = set(nums)
        count = 0
        for num in num_set:
            if num-1 not in num_set:
                count = max(count, count_longest(num))
        return count    