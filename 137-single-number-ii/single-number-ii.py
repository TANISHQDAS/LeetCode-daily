class Solution:
    def singleNumber(self, n):
        o = t = 0
        for x in n:
            t = (t ^ x) & ~o
            o = (o ^ x) & ~t
        return t