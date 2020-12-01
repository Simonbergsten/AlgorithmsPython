"""
What is the maximum we can steal?

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constrains: 0 <= nums.length <= 100
1 <= nums[i] <= 400
"""

# At pos i=2, we can steal the max(dp[1], a[2] + dp[0])

class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.maximum = ["-inf"]


    def rob(self):
        n = len(self.arr)
        if (n == 0):
            return 0

        dp = [0] * n
        dp[0] = self.arr[0]

        for i in range(1, n):
            if (i == 1):
                dp[i] = max(self.arr[0], self.arr[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+self.arr[i])

        self.maximum = dp[n-1]


s = Solution([1,2,3, 1])
s.rob()
print(s.maximum)




