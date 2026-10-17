class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l = [0]*26
        for c in s:
            l[ord(c)-ord('a')]+=1
        for c in t:
            l[ord(c)-ord('a')]-=1
        return l == [0]*26