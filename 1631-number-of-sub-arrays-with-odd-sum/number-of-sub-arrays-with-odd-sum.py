class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        memo = {}

        def dp(i: int, parity: int) -> int:
            if i == n:
                return 0

            if (i, parity) in memo:
                return memo[(i, parity)]

            new_parity = (parity + arr[i]) % 2
            res = new_parity + dp(i + 1, new_parity)
            memo[(i, parity)] = res % mod
            return memo[(i, parity)]

        ans = 0
        for i in range(n):
            ans = (ans + dp(i, 0)) % mod

        return ans