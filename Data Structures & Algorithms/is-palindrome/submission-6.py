class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        lower_s = s.lower()
        for c in lower_s:
            if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                arr.append(c)
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True

