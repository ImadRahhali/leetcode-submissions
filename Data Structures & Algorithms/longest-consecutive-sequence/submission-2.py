class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for i in numSet:
            if (i-1) not in numSet:
                count = 1
                while i+count in numSet:
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount