class Solution:
    def countPS(self, s):
        n = len(s)

        def solve(left, right):
            nonlocal count

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) >= 2:
                    count += 1

                left -= 1
                right += 1

        count = 0

        for i in range(n):
            solve(i, i)

            solve(i, i + 1)

        return count
