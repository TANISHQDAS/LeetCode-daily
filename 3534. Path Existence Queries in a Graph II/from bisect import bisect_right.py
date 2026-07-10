from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        a = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        for i, (_, j) in enumerate(a):
            pos[j] = i

        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1]
            if a[i][0] - a[i - 1][0] > maxDiff:
                comp[i] += 1

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(a, (a[i][0] + maxDiff, n)) - 1

        LOG = n.bit_length()
        up = [nxt]
        for _ in range(LOG - 1):
            p = up[-1]
            up.append([p[p[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            l, r = pos[u], pos[v]
            if l > r:
                l, r = r, l

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            if l == r:
                ans.append(0)
                continue

            cur = l
            d = 0
            for k in range(LOG - 1, -1, -1):
                x = up[k][cur]
                if x < r:
                    cur = x
                    d += 1 << k
            ans.append(d + 1)

        return ans