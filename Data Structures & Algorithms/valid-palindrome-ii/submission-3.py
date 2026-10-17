class Solution:
    def validPalindrome(self, s: str) -> bool:
        k, l, r = 0, 0, len(s) - 1
        while l<r:
            if s[l] == s[r] and k<=1:
                l+=1
                r-=1
            elif (s[l+1] == s[r] or s[l] == s[r-1]) and k<1:
                l+=1
                r-=1
                k+=1
            else:
                return False
        return True