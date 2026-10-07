class Solution:
    def isHappy(self, n: int) -> bool:
        x = set()
        while n != 1 and n not in x:
            x.add(n)
            y = 0
            for i in str(n):
                y += int(i) ** 2
            n = y
        return n == 1