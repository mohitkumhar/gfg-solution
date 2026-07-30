class Solution:
    def solveSudoku(self, mat):

        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]

        empty_cells = []

        # Initialize
        for r in range(9):
            for c in range(9):
                if mat[r][c] == 0:
                    empty_cells.append((r, c))
                else:
                    num = mat[r][c]
                    box_index = (r // 3) * 3 + (c // 3)

                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[box_index][num] = True

        def backtrack(index):
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            for num in range(1, 10):
                if not rows[r][num] and not cols[c][num] and not boxes[box_index][num]:

                    mat[r][c] = num
                    rows[r][num] = cols[c][num] = boxes[box_index][num] = True

                    if backtrack(index + 1):
                        return True

                    mat[r][c] = 0
                    rows[r][num] = cols[c][num] = boxes[box_index][num] = False

            return False

        backtrack(0)