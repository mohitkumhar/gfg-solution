class Solution:
    def uniquePerms(self, arr):
        arr.sort()
        n = len(arr)

        ans = []
        path = []
        used = [False] * n

        def backtrack():
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                # Skip duplicate choices at the same level
                if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(arr[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return ans