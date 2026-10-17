class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occ = Counter(nums)
        n = len(nums)
        res = []
        l = [[] for i in range(n+1)]

        for num in occ:
            l[occ[num]].append(num)

        for i in range(n, 0, -1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res
   