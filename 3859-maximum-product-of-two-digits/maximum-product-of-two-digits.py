class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        ans = 0
        for i in s:
            for j in s:
                if i != j or s.count(i) > 1:
                    ans = max(ans, int(i) * int(j))
        return ans             

        