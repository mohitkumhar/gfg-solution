from collections import deque

class Solution:
    def orangesRot(self, mat):
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        q = deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    q.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, time = q.popleft()
            ans = max(ans, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc, time + 1))

        return ans if fresh_count == 0 else -1