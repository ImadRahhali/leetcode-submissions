class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(filter(str.isalnum, s)).lower()
        l = 0
        r = len(newS)-1
        while l < r :
            if newS[l] != newS[r]:
                return False
            l+=1
            r-=1
        return True
