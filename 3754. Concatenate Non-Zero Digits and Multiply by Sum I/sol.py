class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""
        for i in str(n):
            if i != "0":
                s += i

        if not s:
            return 0

        x = int(s)
        t = 0
        for i in s:
            t += int(i)

        return x * t