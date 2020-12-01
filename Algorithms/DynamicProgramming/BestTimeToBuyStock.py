"""
Only one purchase


"""

class Solution:
    def maxProfit(self, prices):
        buyPrice = float("inf")
        profit = 0

        for i, price in enumerate(prices):
            if (buyPrice > price):
                buyPrice = price
            else:
                profit = max(profit, price-buyPrice)
        return profit

    