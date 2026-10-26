class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l , r = 0 , 1
        while l < r and r <= len(prices) - 1:
            if prices[r] > prices[l] and prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            r += 1
        return profit
                