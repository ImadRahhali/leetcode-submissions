class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m ={}
        for i in range(len(nums)):
            m[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in m and i != m[diff]:
                return sorted([i, m[diff]])
        
            