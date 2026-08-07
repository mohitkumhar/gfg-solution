class Solution:
	def nthRowOfPascalTriangle(self, n):

        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]

        result = [[1], [1, 1]]
        prev = [1, 1]

        for _ in range(3, n + 1):
            currRow = [1]
            j = 1

            while j < len(prev):
                currRow.append(prev[j - 1] + prev[j])
                j += 1
            currRow.append(1)
            result.append(currRow)
            prev = currRow

        return result[-1]
