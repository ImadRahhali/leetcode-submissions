class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxLength = 0
        window = set()
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r+=1
            else:
                window.remove(s[l])
                l+=1
            maxLength = max(maxLength, len(window))
        return maxLength