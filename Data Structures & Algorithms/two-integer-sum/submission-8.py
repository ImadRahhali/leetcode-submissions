class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            dct[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dct and dct[diff] != i:
                return [i, dct[diff]]
                

        