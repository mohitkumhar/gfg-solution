class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        
        low = 0
        high = n

        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2

            time1 = mid * s1
            time2 = (n - mid) * s2

            ans = min(ans, max(time1, time2))

            if time1 < time2:
                low = mid + 1
            else:
                high = mid - 1

        return ans