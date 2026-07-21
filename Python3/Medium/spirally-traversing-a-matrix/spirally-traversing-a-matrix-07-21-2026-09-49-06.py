class Solution:
    def spirallyTraverse(self, mat):
        m = len(mat)
        n = len(mat[0])

        top = 0
        down = m - 1

        left = 0
        right = n - 1

        result = []

        while top <= down and left <= right:
            # for top values
            for i in range(left, right + 1):
               result.append(mat[top][i])
            top += 1

            # for right values
            for i in range(top, down + 1):
                result.append(mat[i][right])
            right -= 1

            # for down values
            if top <= down:
                for i in range(right, left - 1, -1):
                    result.append(mat[down][i])
                down -= 1

            # for left values
            if left <= right:
                for i in range(down, top - 1, -1):
                    result.append(mat[i][left])
                left += 1

        return result
