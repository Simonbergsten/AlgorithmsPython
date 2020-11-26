from typing import List
"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        m = {}
        ans = 0
        sA = len(A)
        sB = len(B)
        sC = len(C)
        sD = len(D)

        for i in range(0, sA):
            x = A[i]
            for j in range(0, sB):
                y = B[j]

                if (x+y not in m):
                    m[x+y] = 0

                m[x+y] += 1

        for i in range(0, sC):
            x = C[i]
            for j in range(0, sD):
                y = D[j]
                target = -(x+y)
                if (target in m):
                    ans += m[target]

        return ans


s = Solution()
ans = s.fourSumCount([1,2], [-2, -1], [-1, 2], [0, 2])
print(ans)

# A = [-1,1]
# B = [1,-1]
# C = [-2,2]
# D = [2,-2]

# A[0] + B[0] + C[0] + D[0] -> -1 + 1 - 2 + 2
# A[1] + B[1] + C[0] + D[0] ->  1  -1 -2 +2
# A[0] + B[0] + C[1] + D[1] -> -1 + 1 + 2 + (-2)
# A[1] + B[1] + C[1] + D[1] -> 1 + (-1) + (-2) + (-2)

b = Solution()
ans_b = s.fourSumCount([-1,1], [1,-1], [-2,2], [2,-2])
print(ans_b)
