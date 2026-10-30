class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:

        MOD = 10 ** 9 + 7
        n = len(arr)

        freq = [0] * (n + 1)

        for x in arr:
            freq[x] += 1

        # Number of elements greater than k
        suffix = n

        product = 1
        ans = 0

        for k in range(r + 1):

            suffix -= freq[k]

            ways = (product * pow(2, suffix, MOD)) % MOD

            if k >= l:
                ans = (ans + ways) % MOD

            product = (
                product * (pow(2, freq[k], MOD) - 1)
            ) % MOD

        return ans
