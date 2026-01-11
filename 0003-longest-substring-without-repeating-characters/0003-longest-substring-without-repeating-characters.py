class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2 :
            return len(s)
        char_set = set()
        st, ed = 0, 0
        count = 0
        while ed<len(s):
            while s[ed] in char_set:
                char_set.remove(s[st])
                st+=1
            
            count = max(count, ed-st+1)

            char_set.add(s[ed])
            ed+=1

        return count