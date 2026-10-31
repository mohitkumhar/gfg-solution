class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        dp0 = arr[0]
        dp1 = arr[0] ** 2

        ans = max(dp0, dp1)

        for i in range(1, len(arr)):
            x = arr[i]

            new_dp1 = max(
                x * x,
                dp0 + x * x,
                dp1 + x
            )

            new_dp0 = max(
                x,
                dp0 + x
            )

            dp0 = new_dp0
            dp1 = new_dp1

            ans = max(ans, dp0, dp1)

        return ans
