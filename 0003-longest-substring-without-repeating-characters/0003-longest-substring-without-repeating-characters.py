class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        i, j = 0, 0
        window_char = set()
        max_window = 0
        while j<len(s):
            while s[j] in window_char:
                window_char.remove(s[i])
                i+=1
            max_window = max(max_window, j-i+1)
            window_char.add(s[j])
            j+=1
        return max_window

