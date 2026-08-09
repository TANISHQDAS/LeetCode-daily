class Solution:
    def partition(self, s):
        res = []
        def dfs(i, p):
            if i == len(s):
                res.append(p[:])
                return
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    p.append(s[i:j + 1])
                    dfs(j + 1, p)
                    p.pop()
        dfs(0, [])
        return res