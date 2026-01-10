class Solution:
    def compare(self, s,t, st,ed):
        print(st, ed)
        for ii in range(ed-st+1):
            if s[st+ii] != t[ii]:
                return False
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        
        st, ed = 0, len(needle)-1

        while ed<len(haystack):
            if self.compare(haystack, needle, st, ed):
                return st
            else:
                st+=1
                ed+=1
        return -1
        