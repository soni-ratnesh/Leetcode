class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2) != (str2+str1):
            return ""
        result = 0
        for ii in range(1,min(len(str1), len(str2))+1):
            if len(str1)%ii ==0 and len(str2)%ii==0:
                result = ii
        return str1[:result]