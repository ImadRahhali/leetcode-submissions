class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return longest_prefix
            longest_prefix += string[i]
        return longest_prefix