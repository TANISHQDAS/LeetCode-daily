class Solution:
    def longestRepeating(self, s: str, q: str, p: List[int]) -> List[int]:
        n = len(s)
        a = list(s)

        mx = [0] * (4 * n)
        pr = [0] * (4 * n)
        sf = [0] * (4 * n)
        lc = [''] * (4 * n)
        rc = [''] * (4 * n)

        def pul(i, l, r):
            x = i * 2
            y = x + 1
            m = (l + r) // 2

            lc[i] = lc[x]
            rc[i] = rc[y]

            pr[i] = pr[x]
            if pr[x] == m - l + 1 and rc[x] == lc[y]:
                pr[i] += pr[y]

            sf[i] = sf[y]
            if sf[y] == r - m and rc[x] == lc[y]:
                sf[i] += sf[x]

            mx[i] = max(mx[x], mx[y])
            if rc[x] == lc[y]:
                mx[i] = max(mx[i], sf[x] + pr[y])

        def bld(i, l, r):
            if l == r:
                mx[i] = pr[i] = sf[i] = 1
                lc[i] = rc[i] = a[l]
                return
            m = (l + r) // 2
            bld(i * 2, l, m)
            bld(i * 2 + 1, m + 1, r)
            pul(i, l, r)

        def upd(i, l, r, p, c):
            if l == r:
                lc[i] = rc[i] = c
                return
            m = (l + r) // 2
            if p <= m:
                upd(i * 2, l, m, p, c)
            else:
                upd(i * 2 + 1, m + 1, r, p, c)
            pul(i, l, r)

        bld(1, 0, n - 1)

        r = []
        for i, c in zip(p, q):
            upd(1, 0, n - 1, i, c)
            r.append(mx[1])

        return r