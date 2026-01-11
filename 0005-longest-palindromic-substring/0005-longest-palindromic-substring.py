class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        max_len = 1
        r = (0,0)

        for ii in range(len(s)-1, -1, -1):
            for jj in range(len(s)-1, ii-1, -1):
                if ii==jj:
                    dp[ii][jj] = 1
                elif s[ii] == s[jj]:
                    if jj-ii == 1 or dp[ii+1][jj-1] == 1:
                        dp[ii][jj] = 1
                        if max_len < abs(jj-ii)+1:
                            max_len = jj-ii+1
                            r = [ii,jj] if jj>ii else [jj,ii]
                    else:
                        dp[ii][jj] = 0
        return s[r[0]:r[1]+1]