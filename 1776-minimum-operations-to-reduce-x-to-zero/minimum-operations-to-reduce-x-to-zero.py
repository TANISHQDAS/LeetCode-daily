class Solution:
    def minOperations(self, a: List[int], x: int) -> int:
        tot = sum(a)
        tgt = tot - x
        n = len(a)

        if tgt < 0:
            return -1
        if tgt == 0:
            return n

        l = 0
        cur = 0
        ans = -1

        for r in range(n):
            cur += a[r]

            while cur > tgt and l <= r:
                cur -= a[l]
                l += 1

            if cur == tgt:
                ans = max(ans, r - l + 1)

        return n - ans if ans != -1 else -1