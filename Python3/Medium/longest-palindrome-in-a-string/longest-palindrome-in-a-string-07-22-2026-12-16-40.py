
class Solution:
    def longestPalindrome(self, s):
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        for L in range(1, n + 1):
            i = 0
            while (i + L - 1) < n:
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                i += 1

        ans = ""

        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    if (j - i + 1) > len(ans):
                        ans = s[i : j + 1]

        return ans
