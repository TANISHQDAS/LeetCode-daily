class Solution:
    def maxProfit(self, p):
        if len(p) < 2:
            return 0
        l = [0] * len(p)
        mn = p[0]
        for i in range(1, len(p)):
            mn = min(mn, p[i])
            l[i] = max(l[i - 1], p[i] - mn)
        r = [0] * len(p)
        mx = p[-1]
        for i in range(len(p) - 2, -1, -1):
            mx = max(mx, p[i])
            r[i] = max(r[i + 1], mx - p[i])
        return max(l[i] + r[i] for i in range(len(p)))