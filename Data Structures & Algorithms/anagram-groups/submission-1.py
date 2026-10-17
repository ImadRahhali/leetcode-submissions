class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anags:
                anags[sorted_s] = [s]
            else:
                anags[sorted_s].append(s)
        return list(anags.values())