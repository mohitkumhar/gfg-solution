class Solution:
    def closestPalindrome(self, num):
        n = len(num)

        # If num itself is a palindrome
        if num == num[::-1]:
            return num

        def make_pal(prefix):
            s = str(prefix)

            if n % 2 == 0:
                return int(s + s[::-1])
            else:
                return int(s + s[:-1][::-1])

        half_len = (n + 1) // 2
        prefix = int(num[:half_len])

        candidates = set()

        # Try prefix - 1, prefix, prefix + 1
        for x in [prefix - 1, prefix, prefix + 1]:
            if x >= 0:
                candidates.add(make_pal(x))

        # Boundary cases
        candidates.add(10 ** (n - 1) - 1)
        candidates.add(10 ** n + 1)

        original = int(num)

        ans = None

        for candidate in candidates:
            if candidate == original:
                continue

            diff = abs(candidate - original)

            if ans is None or diff < abs(ans - original):
                ans = candidate
            elif diff == abs(ans - original):
                ans = min(ans, candidate)

        return str(ans)