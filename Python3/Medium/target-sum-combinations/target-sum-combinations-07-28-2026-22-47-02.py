class Solution:
    def targetSumComb(self, arr, target):

        def backtrack(i, curr_sum, curr_comb):
            nonlocal result
            if curr_sum == target:
                result.append(curr_comb[:])
                return

            if i >= n or curr_sum > target:
                return

            for j in range(i, n):
                curr_sum += arr[j]
                curr_comb.append(arr[j])

                backtrack(j, curr_sum, curr_comb)

                curr_sum -= arr[j]
                curr_comb.pop()

        n = len(arr)

        result = []

        backtrack(0, 0, [])

        return result
