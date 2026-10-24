
class Solution:
    def beautySum(self, s):
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                counts = [f for f in freq if f > 0]

                beauty = max(counts) - min(counts)
                ans += beauty

        return ans
