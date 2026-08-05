from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)
        s = [0] * n
        q = deque([k])
        s[k] = 1
        while q:
            u = q.popleft()
            for v in g[u]:
                if not s[v]:
                    s[v] = 1
                    q.append(v)
        for a, b in invocations:
            if not s[a] and s[b]:
                return list(range(n))
        return [i for i in range(n) if not s[i]]