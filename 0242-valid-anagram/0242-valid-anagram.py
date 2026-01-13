class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            char = [0]*27
            for ii in range(len(s)):
                char[ord(s[ii])-ord('a')]+=1
                char[ord(t[ii])-ord('a')]-=1
            for ii in range(27):
                if char[ii]!=0:
                    return False
            return True
        return False