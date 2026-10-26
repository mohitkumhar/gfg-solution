class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:


        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        m = n - k

        prefix_min = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[n - 1] = suffix_max[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        ans = float('inf')

        for i in range(m + 1):
            if i == 0:
                mn = suffix_min[k]
                mx = suffix_max[k]
            elif i == m:
                mn = prefix_min[i - 1]
                mx = prefix_max[i - 1]
            else:
                mn = min(prefix_min[i - 1], suffix_min[i + k])
                mx = max(prefix_max[i - 1], suffix_max[i + k])

            ans = min(ans, mx - mn)

        return ans
