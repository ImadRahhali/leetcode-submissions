class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) 
        max_count = 0
        for num in s:
            if num-1 not in s:
                curr = num
                counter = 1
                while (curr+1) in s:
                    counter += 1
                    curr = curr + 1
                max_count = max(max_count,counter)
        return max_count