class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        # 0 = unvisited, 1 = visiting, 2 = good, 3 = bad

        def dfs(i):
            if i < 0 or i >= n:
                return True

            if arr[i] == 0:
                state[i] = 3
                return False

            if state[i] == 1:
                return False

            if state[i] == 2:
                return True

            if state[i] == 3:
                return False

            state[i] = 1

            if dfs(i + arr[i]):
                state[i] = 2
                return True

            state[i] = 3
            return False

        ans = 0

        for i in range(n):
            if state[i] == 0:
                if dfs(i):
                    ans += 1
            elif state[i] == 2:
                ans += 1

        return ans