class Solution:
    def betterString(self, s1, s2):
        # Code here
        def countDistinct(s):
            dp = [0] * (len(s) + 1)
            dp[0] = 1

            last = {}

            for i in range(1, len(s) + 1):
                ch = s[i - 1]

                dp[i] = 2 * dp[i - 1]

                if ch in last:
                    dp[i] -= dp[last[ch] - 1]

                last[ch] = i

            return dp[-1]

        count1 = countDistinct(s1)
        count2 = countDistinct(s2)

        return s1 if count1 >= count2 else s2
