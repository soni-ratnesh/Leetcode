from functools import lru_cache

class Solution:
    def validPalindrome(self, s: str) -> bool:  
        @lru_cache
        def check(st, ed, k):
            if ed-st<1:
                return True
            elif s[st] == s[ed]:
                return check(st+1, ed-1, k)
            elif k:
                return check(st, ed-1, k-1) or check(st+1, ed, k-1)
            else:
                return False
        if len(s)<3:
            return True
        return check(0, len(s)-1, 1)