class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from math import comb
        
        def fn(c, r, k):
            w = 1
            for x in c:
                if x > 0:
                    w *= comb(r, x)
                    r -= x
                    if w > k:
                        return k + 1
            return w

        n = len(s)
        m = n // 2
        md = s[m] if n % 2 else ""
        c = [0] * 26
        for ch in s[:m]:
            c[ord(ch) - 97] += 1
            
        if fn(c, m, k) < k:
            return ""

        r = []
        for i in range(m):
            for j in range(26):
                if c[j] > 0:
                    c[j] -= 1
                    w = fn(c, m - 1 - i, k)
                    if w >= k:
                        r.append(chr(97 + j))
                        break
                    k -= w
                    c[j] += 1

        p = "".join(r)
        return p + md + p[::-1]