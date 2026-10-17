class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                p *= nums[j]
            output[i] = p
        return output