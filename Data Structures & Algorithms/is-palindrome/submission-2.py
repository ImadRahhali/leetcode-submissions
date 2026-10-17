class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for c in s.lower():
            if (ord('a') <= ord(c) <= ord('z')) or (ord('0')<=ord(c)<=ord('9')):
                t+=c
        l = 0
        r = len(t) -1
        print(t)
        while l<r:
            if t[l] != t[r]:
                return False
            l+=1
            r-=1
        return True