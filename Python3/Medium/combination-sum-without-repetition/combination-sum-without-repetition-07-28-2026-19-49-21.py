class Solution:
    def uniqueCombinations(self, arr, target):

        def backtrack(i, curr_comb, curr_sum):
            nonlocal result
            if curr_sum == target:
                result.append(curr_comb[:])
                return

            if i >= n or curr_sum > target:
                return

            for j in range(i, n):
                if j > i and arr[j] == arr[j - 1]:
                    continue

                curr_sum += arr[j]
                curr_comb.append(arr[j])

                backtrack(j + 1, curr_comb, curr_sum)

                curr_sum -= arr[j]
                curr_comb.pop()

        result = []
        n = len(arr)
        arr.sort()

        backtrack(0, [], 0)

        return result
