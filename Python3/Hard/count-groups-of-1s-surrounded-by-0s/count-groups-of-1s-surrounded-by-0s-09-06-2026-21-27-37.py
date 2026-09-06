from collections import deque

class Solution:
    def countGroups(self, mat):
        n = len(mat)
        m = len(mat[0])

        valid_groups = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    touches_boundary = False

                    queue = deque([(i, j)])
                    mat[i][j] = 0

                    while queue:
                        r, c = queue.popleft()

                        if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                            touches_boundary = True

                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc

                            if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                                mat[nr][nc] = 0
                                queue.append((nr, nc))

                    if not touches_boundary:
                        valid_groups += 1

        return valid_groups
