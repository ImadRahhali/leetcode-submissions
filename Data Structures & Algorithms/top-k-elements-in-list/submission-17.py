class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        occ = {x:0 for x in nums}
        for i in nums:
            occ[i] += 1
        buckets = {x:[] for x in range(len(nums)+1)}
        for i in occ:
            buckets[occ[i]].append(i)
        for i in range(len(buckets)):
            for i in buckets[len(buckets)-1-i]:
                if len(output) < k:
                    output.append(i)
        return output

