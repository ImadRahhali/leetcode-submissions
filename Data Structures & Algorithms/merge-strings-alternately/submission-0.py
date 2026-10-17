class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        one = 0
        two = 0
        while one < len(word1) and two < len(word2):
            s += word1[one]
            s += word2[two]
            one += 1
            two += 1

        if len(word1) > len(word2):
            s += word1[one:len(word1)+1]
        else:
            s += word2[two:len(word2)+1] 
        
        return s
