class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)

        if total % 2 != 0:
            return []

        target = total // 2
        size1 = n // 2

        def backtrack(i, count, curr_sum, subset):
            if count == size1:
                if curr_sum == target:
                    return subset[:]
                return None

            if i == n or count + (n - i) < size1:
                return None

            subset.append(arr[i])
            result = backtrack(
                i + 1, count + 1, curr_sum + arr[i], subset
            )
            if result is not None:
                return result
            subset.pop()

            return backtrack(i + 1, count, curr_sum, subset)

        first = backtrack(0, 0, 0, [])

        if first is None:
            return []

        # Remove the selected occurrences, handling duplicates correctly.
        remaining = arr[:]
        for x in first:
            remaining.remove(x)

        return [first, remaining]