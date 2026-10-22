class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)

        for i in range(n // 2):
            j = n - 1 - i

            if s[i] != '?' and s[j] != '?' and s[i] != s[j]:
                return -1

        # Replace each mirrored pair with a common character.
        # The optimal replacement must consider adjacent characters.
        # Use DP over the possible letters a-z.
        half = n // 2
        chars = []

        for i in range(half):
            j = n - 1 - i
            if s[i] != '?':
                chars.append(ord(s[i]) - ord('a'))
            elif s[j] != '?':
                chars.append(ord(s[j]) - ord('a'))
            else:
                chars.append(-1)

        # Handle the palindrome's first half and its middle.
        # Each pair contributes twice, except the middle edge.
        dp = [0] * 26

        for i in range(half):
            allowed = range(26) if chars[i] == -1 else [chars[i]]
            new_dp = [float('inf')] * 26

            for c in allowed:
                if i == 0:
                    new_dp[c] = 0
                else:
                    new_dp[c] = min(
                        dp[p] + 2 * abs(p - c)
                        for p in range(26)
                    )

            dp = new_dp

        if n % 2 == 1:
            mid = s[half]
            allowed = range(26) if mid == '?' else [ord(mid) - ord('a')]
            return int(min(
                dp[p] + min(abs(p - c) for c in allowed)
                for p in range(26)
            )) if half else 0

        return int(min(dp)) if half else 0