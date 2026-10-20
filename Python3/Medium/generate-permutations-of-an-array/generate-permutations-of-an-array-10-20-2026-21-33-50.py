class Solution:
    def permuteDist(self, arr):

        ans = []
        path = []
        n = len(arr)
        used = [False] * n

        def backtrack():
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                used[i] = True
                path.append(arr[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return ans