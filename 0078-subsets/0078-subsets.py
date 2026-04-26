class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(index, curr):
            # base case
            if index == n:
                result.append(curr.copy())
                return
            # we can choose index 
            curr.append(nums[index])
            backtrack(index+1, curr)
            curr.pop()

            # now we dont choose index
            backtrack(index+1, curr)



        backtrack(0, [])

        return result
        