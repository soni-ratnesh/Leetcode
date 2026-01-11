class Solution:
    def reverseVowels(self, s: str) -> str:

        vovels = { 'A', 'a', 'E', 'e','I', 'i','O', 'o','U', 'u'}

        ii = 0
        jj = len(s)-1
        result = list(s)

        while (jj-ii) >0:
            if s[ii] in vovels:
                if s[jj] in vovels:
                    result[ii], result[jj] = s[jj], s[ii]
                    ii+=1
                    jj-=1
                else:
                    jj-=1
            else:
                ii+=1
        return "".join(result)


        