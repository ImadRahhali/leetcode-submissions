class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[[],[0],[2],[1,3],[],[]]
        freq = Counter(nums)
        group = [[] for i in range(len(nums)+1)]
        res = []
        for i in freq:
            group[freq[i]].append(i)
        for i in range(len(group)-1, -1, -1):
            if len(res) == k:
                break
            elif len(res)!=k and group[i]!=[]:
                res+=group[i]
        return res
