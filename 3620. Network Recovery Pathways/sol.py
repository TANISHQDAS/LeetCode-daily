from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        d = [0] * n
        hi = 0

        for u, v, w in edges:
            g[u].append((v, w))
            d[v] += 1
            hi = max(hi, w)

        q = deque()
        t = []

        for i in range(n):
            if d[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            t.append(u)
            for v, _ in g[u]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)

        def ok(x):
            inf = 10**18
            dp = [inf] * n
            dp[0] = 0

            for u in t:
                if dp[u] == inf:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in g[u]:
                    if w < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w

            return dp[-1] <= k

        if not ok(0):
            return -1

        l, r = 0, hi
        while l < r:
            m = (l + r + 1) // 2
            if ok(m):
                l = m
            else:
                r = m - 1

        return l