class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        r = 0
        ii, jj = 0, 0 
        while jj<len(s) and ii<=jj:
            while s[jj] in hashset:
                hashset.remove(s[ii])
                ii+=1
            r = max(r, jj-ii+1)    
            hashset.add(s[jj])
            jj+=1
        return r