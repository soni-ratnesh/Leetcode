class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ii = 0
        jj = len(numbers)-1

        while ii<jj:
            t_sum = numbers[ii] + numbers[jj]
            if t_sum == target:
                return [ii+1, jj+1]
            elif t_sum< target:
                ii+=1
            else:
                jj-=1
