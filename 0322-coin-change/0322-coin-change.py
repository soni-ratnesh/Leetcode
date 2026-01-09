class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for ii in range(1, amount+1):
            for coin in coins:
                if coin<=ii:
                    dp[ii] = min(dp[ii], dp[ii-coin]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]
        