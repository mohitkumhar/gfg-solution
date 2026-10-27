class Solution:
    def getMaxWeight(self, s):
        n = len(s)

        # dp[i] = maximum weight for the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Leave the current character unpaired
            dp[i] = dp[i - 1] + 1

            # Pair the last two characters if they are different
            if i >= 2:
                if s[i - 2] != s[i - 1]:
                    dp[i] = max(dp[i], dp[i - 2] + 4)

                else:
                    # Toggle one character to form an alternating pair.
                    # One toggle costs 1, so net pair weight = 4 - 1 = 3.
                    dp[i] = max(dp[i], dp[i - 2] + 3)

        return dp[n]