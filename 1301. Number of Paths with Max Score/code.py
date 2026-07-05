from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        mod = 10**9 + 7

        s = [[-1] * n for _ in range(n)]
        c = [[0] * n for _ in range(n)]
        s[-1][-1] = 0
        c[-1][-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or (i == n - 1 and j == n - 1):
                    continue

                mx = -1
                cnt = 0

                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x < n and y < n:
                        if s[x][y] > mx:
                            mx = s[x][y]
                            cnt = c[x][y]
                        elif s[x][y] == mx and mx != -1:
                            cnt = (cnt + c[x][y]) % mod

                if mx == -1:
                    continue

                if board[i][j] not in "ES":
                    mx += int(board[i][j])

                s[i][j] = mx
                c[i][j] = cnt

        if s[0][0] == -1:
            return [0, 0]

        return [s[0][0], c[0][0]]