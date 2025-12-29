class Solution:
    def isPalindrome(self, s: str) -> bool:
        ii, jj = 0, len(s)-1

        while ii<jj:
            while ii<jj and not s[ii].isalnum():
                ii+=1
            while ii<jj and not s[jj].isalnum():
                jj-=1
            if s[ii].lower()==s[jj].lower():
                ii+=1
                jj-=1
            else:
                return False
        return True