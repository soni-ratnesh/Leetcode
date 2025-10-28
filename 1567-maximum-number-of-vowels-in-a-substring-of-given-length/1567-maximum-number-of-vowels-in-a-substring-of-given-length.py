class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        
        v = {"a","A", "e","E","i","I","O","o","u","U"}
        for ii in range(k):
            if s[ii] in v:
                count+=1
        result = count
        for ii in range(k, len(s)):
            print(ii-k, ii, count)
            if s[ii-k] in v:
                count-=1
            if s[ii] in v:
                count+=1
                result = max(result, count)
        return result
        