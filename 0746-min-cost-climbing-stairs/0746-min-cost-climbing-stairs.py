class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3:
            return min(cost)
        ll_step, l_step = 0, 0

        for ii in range(2,len(cost)+1):

            ll_step, l_step = l_step, min(ll_step+cost[ii-2], l_step+cost[ii-1])
        return l_step