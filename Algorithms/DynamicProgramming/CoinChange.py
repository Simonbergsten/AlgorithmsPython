"""
Find the minimum number of coin change. If no exact change can be found, return -1
"""

class Solution:
    def numCoins(self, coins, amount):
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1

        INT_MAX = 1<<32
        dp = [INT_MAX] * (amount+1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min((dp[i-coin]+1), dp[i])

        return dp[amount] if dp[amount] != INT_MAX else -1

s = Solution()
print(s.numCoins([1,2,5], 11))