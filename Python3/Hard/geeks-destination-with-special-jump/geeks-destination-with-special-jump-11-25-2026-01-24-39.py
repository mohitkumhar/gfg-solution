class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        # code here

        MOD = 10**9 + 7
        c = a - b

        # Time required without using a jump
        kd = (d - a + c - 1) // c
        normal = d + 2 * b * kd

        # Prefix sum of cycle counts
        def prefix_k(n):
            if n <= a:
                return 0

            m = n - a
            q, rem = divmod(m, c)

            return c * q * (q + 1) // 2 + rem * (q + 1)

        # Prefix sum of jump-based times
        def prefix_time(n):
            return n * (n + 1) // 2 + n + 2 * b * prefix_k(n)

        # Find the largest x where jumping is better
        low, high = 1, d
        cutoff = 0

        while low <= high:
            mid = (low + high) // 2

            k = max(0, (mid - a + c - 1) // c)
            jump_time = mid + 2 * b * k + 1

            if jump_time < normal:
                cutoff = mid
                low = mid + 1
            else:
                high = mid - 1

        # Convert jump lengths into positions
        L = d - r
        R = d - l

        # Positions where using a jump is better
        x1 = L
        x2 = min(R, cutoff)

        ans = 0

        if x1 <= x2:
            ans += prefix_time(x2) - prefix_time(x1 - 1)

        # Remaining positions use normal movement
        y1 = max(L, cutoff + 1)
        y2 = R

        if y1 <= y2:
            ans += (y2 - y1 + 1) * normal

        return ans % MOD
