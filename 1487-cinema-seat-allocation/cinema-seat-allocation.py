class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        d = {}
        for x, y in r:
            d[x] = d.get(x, 0) | (1 << y)

        a = (n - len(d)) * 2

        p = sum(1 << i for i in range(2, 6))
        q = sum(1 << i for i in range(4, 8))
        z = sum(1 << i for i in range(6, 10))

        for m in d.values():
            u = not (m & p)
            v = not (m & q)
            w = not (m & z)

            if u and w:
                a += 2
            elif u or v or w:
                a += 1

        return a