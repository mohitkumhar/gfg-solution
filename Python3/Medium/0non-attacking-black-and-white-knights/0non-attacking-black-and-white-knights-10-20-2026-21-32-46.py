class Solution:
    def numOfWays(self, n, m):
        total_squares = n * m

        # Place black and white knights on distinct squares
        total_ways = total_squares * (total_squares - 1)

        # Count attacking pairs
        attacking = 0

        # A knight attacks using 2x1 or 1x2 moves
        attacking += 2 * max(0, n - 2) * max(0, m - 1)
        attacking += 2 * max(0, n - 1) * max(0, m - 2)

        # Each attacking pair has two color arrangements
        attacking *= 2

        return total_ways - attacking
