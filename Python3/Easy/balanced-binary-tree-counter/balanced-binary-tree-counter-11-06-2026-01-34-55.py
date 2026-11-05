class Solution:
    def countBT(self, h: int) -> int:
        # code here
        MOD = 10 ** 9 + 7

        if h == 0:
            return 1

        if h == 1:
            return 1

        prev2 = 1  # dp[0]
        prev1 = 1  # dp[1]

        for i in range(2, h + 1):
            curr = (
                prev1 * prev1 +
                2 * prev1 * prev2
            ) % MOD

            prev2 = prev1
            prev1 = curr

        return prev1
