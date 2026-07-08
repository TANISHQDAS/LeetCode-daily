from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        ans = []

        for l, r in queries:
            x = 0
            sm = 0
            for c in s[l:r + 1]:
                if c != "0":
                    d = ord(c) - 48
                    x = (x * 10 + d) % mod
                    sm += d
            ans.append(x * sm % mod)

        return ans