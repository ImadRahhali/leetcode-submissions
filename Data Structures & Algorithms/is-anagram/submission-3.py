class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[ord(c) - ord('a')] = count.get(ord(c) - ord('a'),0) + 1
        for c in t:
            count[ord(c) - ord('a')] = count.get(ord(c) - ord('a'),0) - 1
        for i in count.values():
            if i!=0:
                return False
        return True
