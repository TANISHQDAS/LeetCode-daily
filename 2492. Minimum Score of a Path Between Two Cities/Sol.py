from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for a, b, w in roads:
            g[a].append((b, w))
            g[b].append((a, w))

        vis = [0] * (n + 1)
        ans = 10**9

        def dfs(u):
            nonlocal ans
            vis[u] = 1
            for v, w in g[u]:
                ans = min(ans, w)
                if not vis[v]:
                    dfs(v)

        dfs(1)
        return ans