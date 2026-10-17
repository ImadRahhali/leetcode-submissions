class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets = "qwertyuiopasdfghjklzxcvbnm"
        m = {}
        for c in alphabets:
            m[c] = 0
        for c1 in s:
            m[c1] += 1
        for c2 in t:
            m[c2] -= 1
        
        for i in m.values():
            if i != 0:
                return False
        
        return True