class Solution:
    def maxProfit(self, p):
        mn = float('inf')
        mx = 0
        for pr in p:
            mx = max(mx, pr - mn)
            mn = min(mn, pr)
        return mx