class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s):
            ii = 0

            for jj in range(len(t)):
                if s[ii] == t[jj]:
                    ii+=1
                if ii == len(s):
                    return True

            return False
        else:
            return True