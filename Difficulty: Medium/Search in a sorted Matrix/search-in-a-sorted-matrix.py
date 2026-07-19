class Solution:
    def searchMatrix(self, mat, x):
        m = len(mat)
        n = len(mat[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mat[mid // n][mid % n]

            if mid_val == x:
                return True

            elif mid_val > x:
                right = mid - 1
            else :
                left = mid + 1

        return False
