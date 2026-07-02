from collections import deque


class Solution:
    def findSafeWalk(self, g, h):
        r, c = len(g), len(g[0])
        q = deque([(0, 0, h - g[0][0])])
        vis = [[-1] * c for _ in range(r)]

        while q:
            x, y, hp = q.popleft()
            if hp <= vis[x][y] or hp < 1:
                continue
            vis[x][y] = hp

            if x == r - 1 and y == c - 1:
                return True

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    q.append((nx, ny, hp - g[nx][ny]))

        return False
