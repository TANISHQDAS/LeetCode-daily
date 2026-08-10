class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        d = [False] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not d[i - j * j]:
                    d[i] = True
                    break
                j += 1
        return d[n]