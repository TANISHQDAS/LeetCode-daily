class Solution:
    def generate(self, n):
        res = []
        for i in range(n):
            r = [1]
            if res:
                for j in range(len(res[-1]) - 1):
                    r.append(res[-1][j] + res[-1][j + 1])
                r.append(1)
            res.append(r)
        return res