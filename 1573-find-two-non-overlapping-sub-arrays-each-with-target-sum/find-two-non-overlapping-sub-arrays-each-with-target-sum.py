class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        mp = {0: 0}
        sm = 0
        n = len(arr)
        mn = [float('inf')] * (n + 1)
        ans = float('inf')

        for i, v in enumerate(arr, 1):
            sm += v
            mn[i] = mn[i - 1]
            r = sm - target

            if r in mp:
                j = mp[r]
                l = i - j
                mn[i] = min(mn[i], l)
                ans = min(ans, mn[j] + l)

            mp[sm] = i

        return -1 if ans > n else ans