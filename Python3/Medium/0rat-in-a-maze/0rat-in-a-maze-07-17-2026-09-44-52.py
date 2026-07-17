class Solution:
    def ratInMaze(self, maze):

        def solve(i, j, curr_path):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if maze[i][j] != 1:
                return

            if i == m - 1 and j == n - 1:
                result.append("".join(curr_path))
                return

            maze[i][j] = 0
            # down
            curr_path.append("D")
            solve(i + 1, j, curr_path)
            curr_path.pop()

            # up
            curr_path.append("U")
            solve(i - 1, j, curr_path)
            curr_path.pop()

            # left
            curr_path.append("L")
            solve(i, j - 1, curr_path)
            curr_path.pop()

            # right
            curr_path.append("R")
            solve(i, j + 1, curr_path)
            curr_path.pop()

            maze[i][j] = 1

        m = len(maze)
        n = len(maze[0])

        if maze[0][0] != 1:
            return []

        result = []
        solve(0, 0, [])

        return sorted(result)
