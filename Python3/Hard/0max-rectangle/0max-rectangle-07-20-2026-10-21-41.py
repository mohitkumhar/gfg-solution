from typing import List

class Solution:
    def maxArea(self, mat):

        def find_histogram(heights: List[int]) -> int:
            n = len(heights)
            left_smaller_val = []
            stack = []

            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()

                if not stack:
                    left_smaller_val.append(-1)
                elif heights[stack[-1]] < heights[i]:
                    left_smaller_val.append(stack[-1])

                stack.append(i)

            right_smaller_val = []
            stack = []

            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()

                if not stack:
                    right_smaller_val.append(n)
                elif heights[stack[-1]] < heights[i]:
                    right_smaller_val.append(stack[-1])

                stack.append(i)
            right_smaller_val.reverse()
            max_area = 0

            for i in range(n):
                width = right_smaller_val[i] - left_smaller_val[i] - 1
                curr_area = heights[i] * width

                max_area = max(max_area, curr_area)

            return max_area

        m = len(mat)
        n = len(mat[0])
        max_area = 0

        heights = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            curr_area = find_histogram(heights)
            max_area = max(max_area, curr_area)

        return max_area
