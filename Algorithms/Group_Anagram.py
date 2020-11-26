"""
# Time Complexity O(N * M * Log(M))
# N: Length of the input array
# M: Length of biggest string in the array
# M*Log(M) is due to the fact that we sort each string when we pass over it in the loop.
"""


class Solution:

    def findHash(self, s):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs):
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if hashed not in m:
                m[hashed] = []
            m[hashed].append(s)

        for p in m.values():
            answers.append(p)

        return answers


s = Solution()
answers = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(answers)
