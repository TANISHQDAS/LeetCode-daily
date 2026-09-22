class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = 1
        while m < n:
            m <<= 1
        p = [1] * (2 * m)
        c = [[0] * k for _ in range(2 * m)]
        for i in range(n):
            v = nums[i] % k
            p[m + i] = v
            c[m + i][v] = 1

        def up(u):
            l = u << 1
            r = l | 1
            pl = p[l]
            p[u] = (pl * p[r]) % k
            cx = list(c[l])
            cr = c[r]
            for j in range(k):
                cx[(pl * j) % k] += cr[j]
            c[u] = cx

        for i in range(m - 1, 0, -1):
            up(i)

        ans = []
        for idx, val, st, tgt in queries:
            u = m + idx
            v = val % k
            p[u] = v
            c[u] = [0] * k
            c[u][v] = 1
            u >>= 1
            while u > 0:
                up(u)
                u >>= 1

            l = m + st
            r = m + n
            lt = []
            rt = []
            while l < r:
                if l & 1:
                    lt.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    rt.append(r)
                l >>= 1
                r >>= 1

            cp = 1
            cc = [0] * k
            for nd in lt + rt[::-1]:
                nc = list(cc)
                cu = c[nd]
                for j in range(k):
                    nc[(cp * j) % k] += cu[j]
                cc = nc
                cp = (cp * p[nd]) % k

            ans.append(cc[tgt])

        return ans