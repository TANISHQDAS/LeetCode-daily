class Solution:
    def maxPoints(self, p):
        from math import gcd
        if len(p) <= 2:
            return len(p)
        mx = 0
        for i in range(len(p)):
            sl = {}
            for j in range(len(p)):
                if i == j:
                    continue
                dx = p[j][0] - p[i][0]
                dy = p[j][1] - p[i][1]
                g = gcd(dx, dy)
                k = (dx // g, dy // g)
                sl[k] = sl.get(k, 0) + 1
            mx = max(mx, max(sl.values()) + 1 if sl else 1)
        return mx