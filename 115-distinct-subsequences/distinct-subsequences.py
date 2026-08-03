class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        d = [1] + [0] * m
        for c in s:
            for i in range(m - 1, -1, -1):
                if c == t[i]:
                    d[i + 1] += d[i]
        return d[m]