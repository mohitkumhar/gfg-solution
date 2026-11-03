class Solution:
    def subarrayXor(self, A):
        N = len(A)
        ans = 0

        for i in range(N):
            count = (i + 1) * (N - i)

            if count % 2 == 1:
                ans ^= A[i]

        return ans
