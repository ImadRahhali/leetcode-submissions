class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]
        for i in range(n-1, -1, -1):
            res[i] = suffix * res[i]
            suffix = suffix * nums[i]
        return res