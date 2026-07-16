class Solution:
    def isWordExist(self, mat, word):

        def backtrack(i: int, j: int, idx: int):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or mat[i][j] == "$":
                return False
            if mat[i][j] != word[idx]:
                return False

            temp = mat[i][j]
            mat[i][j] = "$"

            for dirx, diry in directions:
                newI = i + dirx
                newJ = j + diry

                if backtrack(newI, newJ, idx + 1):
                    return True

            mat[i][j] = temp

        m = len(mat)
        n = len(mat[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False