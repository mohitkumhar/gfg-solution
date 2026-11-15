class Solution:

    def subsequenceSum(self, s):
        """code here"""

        MOD = 10 ** 9 + 7

        digitSum = sum(int(ch) for ch in s)

        return (digitSum * pow(2, len(s) - 1, MOD)) % MOD
