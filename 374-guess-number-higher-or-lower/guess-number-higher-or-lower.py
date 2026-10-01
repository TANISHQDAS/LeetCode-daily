class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            x = guess(m)

            if x == 0:
                return m
            elif x == -1:
                r = m - 1
            else:
                l = m + 1