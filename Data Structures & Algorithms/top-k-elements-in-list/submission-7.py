class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        group = [[] for i in range(len(nums)+1)]
        res = []
        for i in freq:
            group[freq[i]].append(i)
        for i in range(len(group)-1, 0, -1):
            for num in group[i]:
                res.append(num)
            if len(res) == k:
                return res
